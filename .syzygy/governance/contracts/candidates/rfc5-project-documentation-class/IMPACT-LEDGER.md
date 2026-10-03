> **Candidate — binds nothing.** The blast-radius ledger for
> `SEMANTIC-DELTA.md`. It restates no act and is evidence of a sweep, valid
> for the commit it names.

# Impact ledger — RFC5-14 `project-documentation` class

**Commit swept:** `9a6e8e31cfa842e83fa0970765f581579b40de3b` (`git ls-tree -r -z`), the `origin/main` this package was rebased onto for round 2.
**Denominator:** 1988 tracked files; 1984 decode as UTF-8 and were searched; 4 did not.
Round 1 swept `dbf8ed1911aa193b0db7cfebdf8d4338c7500ba0` (1973 files, 4 not UTF-8) and published B as 83 and the union as 141. Re-run in round 2 by script at both commits, the predicate below gives A = 78, B = 82, A∩B = 20, A∪B = 140 and C = 7 at both. Round 1's B (83) and union (141) are not reproduced by the stated rule.

## The three sweeps, as run

| Predicate | Rule (Python `re`, case-sensitive) | Files at `9a6e8e31` |
|---|---|---|
| A. names a class | `\b(governance-text\|code-structure\|code-content\|work-history\|evidence-content\|derived-composites)\b` | 78 |
| B. cites RFC5-14 | run form `RFC5-(\d+)((?:\s*(?:,\|/\|\.\.\|…\|–\|and\|or)\s*(?:RFC5-)?\d+)*)`, then the span rule below | 82 |
| C. enumerates the vocabulary | at least four of the six class names appear in the file | 7 |

**Span rule for B.** Take each match of the run form. Read it as a head number
and a sequence of (separator, number) pairs, each separator read from the
match text and each number the one that follows it. The match counts when the
head or any listed number is 14, or when some *adjacent* pair, whose separator
is `..`, `…` or `–`, has 14 between its two numbers inclusive. Nothing else
counts: in `RFC5-1..RFC5-11, RFC5-24..RFC5-26` the pairs are (1..11), (11, 24)
and (24..26), and 14 lies in none, so the file is not counted. Whitespace in
the run form includes a line break, so a citation wrapped across lines is
read; a file counts once however many matches it holds. A variant that takes
the minimum to the maximum of the whole match instead counts one more file
(a `round-2026-08c` raw), which this ledger does not use.

A and B overlap in 20 files; their union is 140 (78 + 82 - 20). B over-counts
on purpose: a range such as the whole-module span `RFC5-1..27` counts, and so
does any list containing 14. A second method (C) and a path grouping below
classify the 140. Every figure above was derived by script at the commit
named, not copied from the round-1 review.

## Classification of the union (140)

Groups are assigned by the first matching path prefix, in this order, so each
file lands in exactly one group.

| Group (path rule) | Files | Reading |
|---|---|---|
| Installed RFC modules (`.syzygy/governance/contracts/rfcs/`) | 9 | Only `RFC-0005/consent-egress-secrets.md` carries the vocabulary table; the rest cite RFC5-14 or use `code-structure` as an adapter name (RFC-0004). Unchanged |
| Mirrored RFC modules (`contracts/candidates/rfcs/`) | 15 | Same reading, identical mirror |
| Readability restyle package (`contracts/candidates/contract-readability-restyle/`) | 9 | Performed-act history for the restyle, including a patch of the module's earlier text. Not edited |
| History (`contracts/candidates/history/`) | 6 | Non-authoritative history; not edited |
| Rounds (`contracts/candidates/round-*`) | 23 | Non-authoritative history; not edited |
| Review raws (`docs/reviews/`, `contracts/candidates/reviews/`) | 14 | Spent evidence; not edited |
| Evidence records (`docs/evidence/`) | 10 | Spent evidence; not edited |
| Pursuit data (`docs/pursuits/`) | 4 | Spent evidence; not edited |
| OpenSpec (`openspec/`) | 9 | One enumerates the six (below); the rest cite by reference |
| Code (`apps/`, `packages/`) | 20 | None enumerates the six: every one of the 20 names only `code-structure`, a POC module and adapter name |
| Docs (`docs/`, other) | 6 | Cite by reference or describe the gap |
| Decision (`.syzygy/governance/decisions/`) | 1 | Cites by reference |
| Generated (`DIRECTIVE-REGISTER.md`) | 1 | Regenerates after adoption, never before |
| Other candidate, bound contract and map material (rest of `.syzygy/`) | 13 | Cite RFC5-14 by number; unaffected by a new row |

Counts sum to the union: 9+15+9+6+23+14+10+4+9+20+6+1+1+13 = 140.

## Findings that need an owner's attention

1. `openspec/changes/polaris-manifesto-generation/SOURCE-POLICY.md` enumerates
   the six classes with "remains". It is bound by performed acts (the
   adoption and the base readability successor name it), so it cannot be
   edited. It goes stale on adoption. Options are in `SEMANTIC-DELTA.md`,
   migration step 2.
2. `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
   (REQ-polaris-generation-025) cites RFC5-14's vocabulary by reference and
   says no class order is invented. Consistent with the proposed text; no edit.
3. [Observed] RFC5-14's "highest class" has no defined order; the spec states
   none is to be invented. The proposed text adds none and says so. A reviewer
   may rule that sentence insufficient; that would be a contract question about
   the existing "highest" wording, outside this delta.

## Digest-bound neighbours

The module is a row of the bootstrap manifest and is also covered by the
readability restyle link. The proposed manifest here hashes proposed bytes and
matches the tree only after adoption. Regenerating this package's manifest
retires any copy of its digest.
