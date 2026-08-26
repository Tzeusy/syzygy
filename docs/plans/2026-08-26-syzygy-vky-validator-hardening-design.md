# syzygy-vky validator hardening design

**Status:** Approved by the owner on 2026-08-26.

## Outcome

Narrow `syzygy-vky` to two process-housekeeping corrections in the existing
governance checker:

1. An installed shape-M reference classified under CG-1i must resolve from
   the corresponding candidate source location. The warning remains honest
   only while that fallback is real.
2. CG-7d must report its quotation denominator per digest-bearing subject, so
   a subject with zero current quotations is disclosed rather than hidden by
   the aggregate population.

The implementation owns only `scripts/check_governance.py`. It adds no check
family, governed artifact, dependency, or runtime behavior.

## Authority and boundaries

The change is process housekeeping under the repository operating procedure.
It serves:

- VIS-7's internal-link trust floor by testing the shape-M fallback that makes
  installed references resolvable through their candidate twins.
- VIS-2's evidence rule by exposing a zero subject denominator rather than
  allowing unrelated quotations to imply coverage.
- The owner's P-33 shape-M decision. Installed modules remain intentionally
  non-self-contained; this change verifies the selected fallback instead of
  replacing it.

The following remain out of scope:

- edits to accepted RFC 0001-0009, candidate RFC 0010/0011, D3, acceptance
  records, owner-decision registers, or frozen round records;
- rulings on P-15 or P-21;
- creating a D3 quotation, a golden convergence report, or a historical
  annotation merely to increase a denominator;
- changing shape M or copying companion artifacts into the installed tree;
- any work from `syzygy-2dn`, which remains held because it mixes act-bound
  policy amendments, open owner gates, superseded history, and deferred waves.

## Design

### CG-1i candidate fallback

Keep the existing link classification order. A declared-forward target stays
in its existing forward-reference class. For an installed-tree path that does
not resolve beside the installed module, derive the corresponding candidate
module and evaluate the same relative reference there.

- If the candidate twin exists and the reference resolves from it, retain the
  disclosed CG-1i warning and count the reference.
- If the candidate twin is absent, fail the check.
- If the candidate twin exists but the same reference is missing or uses the
  wrong depth, fail the check.

The fallback must be derived from the established accepted-to-candidate path
mapping, not from a new allowlist of known files. This keeps newly installed
modules inside the predicate automatically.

### CG-7d subject denominators

Retain the existing digest-comparison semantics. Change the reporting model so
each registered digest-bearing subject has its own examined count and finding
count before the aggregate result is formed.

A zero count is disclosed for that subject. It is not itself a stale-digest
failure, because an unoffered act may lawfully have no quotation, but the
overall report must not describe the aggregate as unqualified `OK` while a
registered subject has no evidence population. Introducing a quotation with a
stale digest remains a failure against that subject's current digest.

## Failure behavior

| Condition | Required result |
|---|---|
| Installed reference resolves only through its candidate twin | CG-1i warning with an explicit examined count |
| Candidate twin is absent | Failure |
| Candidate twin exists but its relative reference is unresolved | Failure |
| Reference is an established declared-forward target | Existing forward-reference classification |
| Registered digest subject has zero current quotations | Per-subject zero disclosed; aggregate not unqualified `OK` |
| Quotation carries a stale digest | Failure against the named subject |
| Other subjects have quotations while one subject has zero | The zero remains visible and cannot be masked by the aggregate |

## Verification

Add behavior-executing selftest fixtures for:

- a valid candidate fallback;
- a missing candidate twin;
- a wrong-depth or unresolved candidate fallback;
- one registered digest subject with zero quotations while another is
  nonzero;
- a stale D3-form quotation.

During implementation:

1. Run the focused selftest cases while iterating.
2. Run `python3 scripts/check_governance.py --scope tracked` and inspect the
   CG-1i and CG-7d output and denominators.
3. Run `python3 scripts/check_governance.py --selftest` and confirm the new
   mutations apply and the intended predicates fail.
4. Independently enumerate installed fallback pairs and per-subject digest
   quotations, then compare their denominators with checker output.
5. Before completion, run the canonical `PROJECT-STATUS.md` battery in a clean
   clone at the exact commit and inspect command output, not only exit codes.

The canonical battery command list does not change, so `PROJECT-STATUS.md`
requires no edit.

## Rollback

The change is confined to one checker and its inline fixtures. Reverting its
single implementation commit restores the previous warning/reporting behavior
without changing governed bytes or repository data.
