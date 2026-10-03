> **Candidate — binds nothing.** The blast-radius ledger for
> `SEMANTIC-DELTA.md`. It restates no act and is evidence of a sweep, valid
> for the commit it names.

# Impact ledger — RFC5-14 `project-documentation` class

**Commit swept:** `dbf8ed1911aa193b0db7cfebdf8d4338c7500ba0` (tracked files, `git ls-files -z`).
**Denominator:** 1973 tracked files; 1969 decode as UTF-8 and were searched; 4 did not.

## The three sweeps, as run

| Predicate | Regex (Python `re`, case-sensitive) | Files |
|---|---|---|
| A. names a class | `\b(governance-text\|code-structure\|code-content\|work-history\|evidence-content\|derived-composites)\b` | 78 |
| B. cites RFC5-14 | `RFC5-(\d+)((?:\s*(?:,\|/\|\.\.\|…\|–\|and\|or)\s*(?:RFC5-)?\d+)*)`; counted when 14 is a listed number or lies inside a `..`/`…`/`–` range | 83 |
| C. enumerates the vocabulary | at least four of the six class names appear in the file | 7 |

A and B overlap in 20 files; their union is 141. Predicate B over-counts on
purpose: a range such as the whole-module span `RFC5-1..27` counts, and so does
any list containing 14. A second method (C) and a per-file reading below
classify the 141.

## Classification of the union (141)

| Group | Files | Reading |
|---|---|---|
| Installed and mirrored RFC-0003/4/5/7 modules | 9 installed, 15 mirror | Only `RFC-0005/consent-egress-secrets.md` (both mirrors) carries the vocabulary table; the rest cite RFC5-14 or use `code-structure` as an adapter name (RFC-0004). Unchanged |
| The same module's restyle patch | 1 (contract-readability-restyle proposed) | Performed-act history for the restyle; a patch of the module's earlier text. Not edited |
| Other candidate and bound contract material | 24 (candidates dir, matrices, ledgers, topology candidates) | Cite RFC5-14 by number; unaffected by a new row |
| History and rounds | 6 history, 24 round-* | Non-authoritative history; not edited |
| Raw reviews and evidence | 11 review raws, 10 evidence records, 4 pursuit data | Spent evidence; not edited |
| OpenSpec | 9 | One enumerates the six (below); the rest cite by reference |
| Code | 20 | None enumerates the six (predicate C finds no code file); strings name unrelated models |
| Docs and one decision | 6 docs, 1 decision | Cite by reference or describe the gap |
| Generated | 1 (`DIRECTIVE-REGISTER.md`) | Regenerates after adoption, never before |

Counts in the table sum to the union: 9+15+1+24+6+24+11+10+4+9+20+6+1+1 = 141.

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
