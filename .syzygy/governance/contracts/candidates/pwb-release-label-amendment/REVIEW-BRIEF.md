# Review brief — PWB release-label amendment

> **Candidate — binds nothing.** This brief tells a fresh-context reviewer
> what to read and what to decide. It is not itself under review.

## What you are reviewing

One amendment package against the signed PWB specification,
`openspec/changes/polaris-project-wide-butlers-model/`. It consists of:

- the five patches under `proposed/`;
- the manifest `PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt`;
- `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md` in
  this directory;
- the builder `scripts/build_pwb_release_label_amendment.py`.

To read the proposed bytes, run `python3
scripts/build_pwb_release_label_amendment.py --diff`, or apply the patches in
a scratch copy. Never apply them in the tree.

## Governing references (read only these)

- **The direction.** It is quoted in full in `SEMANTIC-DELTA.md` §"The
  warrant". It lives on bead `syzygy-l362` and is not a tracked file.
- **The signed subject.** The eleven artifacts the manifest names. Their
  current bytes are those signed at
  `.syzygy/governance/decisions/PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md`.
- **The sign-off scope.**
  `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`.
- **The specification bar.** CC-SPEC-1…11 in
  `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`.
  It is in force despite the path, because craft acts 6 and 7 bound it.
- **The clauses relied on:**
  - RFC2-2 in `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`;
  - RFC2-24 in `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`;
  - RFC4-11 in `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`;
  - RFC6-15 in `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`;
  - RFC1-10 in `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`,
    as an analogy only.
- **The observer's read authority.**
  `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`.
- **Doctrine.** VIS-2, VIS-3 and VIS-7 in `.syzygy/governance/doctrine/vision.md`.

## Acceptance criteria

1. **Direction content.** The package carries what the direction asks for
   Polaris:
   - the release label leads;
   - the object id sits beneath it as the identity;
   - a moved tag is detected, not trusted;
   - an untagged commit shows a short id, honestly labelled.

   Every departure from the direction is named and put to the owner: the read
   change, Trajectory and Orrery, the limits of moved-tag detection, and the
   tag population.
2. **The specification bar.** The amended requirement meets CC-SPEC: one
   obligation form, scope, a sweep oracle with a denominator, an observable,
   oracle independence, a falsifier, and scenarios its text carries. The
   four-form rule decides every revision without judgment.
3. **Contract claims.** Each claim is anchored to a defined clause and quoted
   (rule 8). No contract-coverage row claims something the oracle does not
   observe, and the claim that no coverage row moves is true.
4. **Signed bytes.** No signed byte outside the patches changes. Every
   requirement but PWB-REQ-001 is byte-identical, and PWB-REQ-001's signed
   text and scenario survive.
5. **Mechanics.**
   - `--check` and `--selftest` pass, and each selftest mutant fails on its
     own predicate (rule 6).
   - The dependency file equals regeneration.
   - `scripts/build_polaris_project_wide_contract_coverage.py --check` passes
     over the proposed bytes.
   - The capability totals equal computation.
6. **Honest claims.** The package claims no adoption, authorizes no read,
   schedules no implementation, and names the residuals the sign-off change
   must carry.
7. **Plain language.** A fresh reader can restate what changes and what does
   not (VIS-3).

Run the checks in a clone, not this worktree (verification rule 7):

- `python3 scripts/build_pwb_release_label_amendment.py --check`
- `python3 scripts/build_pwb_release_label_amendment.py --selftest`
- `python3 scripts/check_governance.py`

## Output contract

Write your raw output verbatim to the path the dispatcher names; the
filename ends in `-RAW.md`. The first four non-blank lines must be exactly
these:

```text
# <title>
Reviewed commit: <40-hex commit you read>
Manifest SHA-256: <sha256 of PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt, the file>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of the manifest **file** at the reviewed
commit, computed by script. It is not any row inside the manifest.

Then add a `## Findings` section, numbering findings as
`**Finding N — title** (blocking|revise|note)`. CONFIRM WITH EXCEPTIONS means
every finding is a `note`.
