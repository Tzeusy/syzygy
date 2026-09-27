> **Candidate — binds nothing.** This ledger describes the proposed readability
> successor and performs no act.

# Impact ledger — Three-Surface POC readability successor

Baseline: `3c915991fbb0eebc38f8daaaea4d05679914b6b8`.

## Discovery method

[Observed] A Python regular-expression sweep ran over all 1,555 paths from
`git ls-files -z`. Of those, 1,551 decoded as UTF-8 and four PNG evidence files
were binary remainders. The decoded population contains 1,121 full
`POC-REQ-NNN` occurrences in 121 files.

The full-form file population partitions as:

| Class | Files | Disposition |
|---|---:|---|
| Signed POC package | 6 | Four proposed rows move; two remain byte-identical |
| Implementation and scripts | 22 | Stable IDs still resolve; no code changes |
| Reviews and evidence | 58 | Historical/retained; never rewritten to current prose |
| Other governance | 14 | Acts and routing retain stable identities |
| Other documentation | 21 | Stable citations remain valid; no normative restatement repair |

A fixed-string `git grep -l -F` sweep per requirement ID is the independent
confirmation method required before review. The final ledger must enumerate any
continuation/run form the full-ID sweep misses rather than publishing an
absence from one spelling.

## Signed subject

| Subject | Proposed result |
|---|---|
| `.openspec.yaml` | unchanged |
| `proposal.md` | answer-first rationale, scope and non-goals |
| `design.md` | answer-first shared-model/data-flow tree and diagram |
| `specs/three-surface-poc-experience/spec.md` | 24 answer-first requirement bodies; normalized normative words preserved |
| `CONTRACT-COVERAGE.md` | unchanged |
| `GOVERNING-DEPENDENCIES.md` | regenerated Source digest; requirement/warrant union unchanged |

The manifest always carries all six rows, sorted. `tasks.md` is deliberately
outside the predecessor act and this successor.

## Consumers and trust boundary

No implementation consumer changes. The candidate reads only tracked Syzygy
authority. It performs no provider call, repository body read, database read,
write, deployment or runtime effect.

The stable requirement identities continue to serve all implementation,
review, evidence and documentation citers. Historical reviews remain accurate
about the bytes they reviewed and are not updated to the successor wording.

## Failure and ordering

- A missing, duplicate, renamed or reordered requirement/scenario fails.
- A normalized normative-body difference fails.
- A warrants difference fails.
- A changed coverage or `.openspec.yaml` row fails.
- Dependency regeneration or manifest drift fails.
- Partial patch application fails.
- A same-subject branch discovered before review serializes this candidate.

There is no active direct POC-package PR at the baseline. Recheck immediately
before review. Candidate checks are pure and repeatable; `--apply` is guarded
for a later owner-act recorder only.

## Documentation and battery

No default current-state page changes during drafting. The candidate builder is
run directly. Per the repository's CG-26 rule, canonical PROJECT-STATUS and
hosted-workflow registration is deferred to the parent sub-epic's single
integration/reconciliation change.
