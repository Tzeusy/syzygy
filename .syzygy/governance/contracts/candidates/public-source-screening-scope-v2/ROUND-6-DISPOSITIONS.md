# Round 6 dispositions — public-source screening scope, version 2

> **Candidate — binds nothing.** Record for
> `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-6-RAW.md` (verdict REVISE;
> finding R6-1 revise, R6-2 to R6-4 notes), written 2026-10-04. The raw is
> retained verbatim. No digest is copied here.

## Stopping rule

Round 6 was agreed as the last round. This record dispatches no round 7. The
recorder stays unfrozen: it records only a confirming review (CONFIRM, or
notes-only CONFIRM WITH EXCEPTIONS) that binds the manifest file. The owner is
asked whether to run one more narrow review of the repair below or to leave the
act for a later sitting.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-source-screening-scope-v2/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-6-RAW.md
Revise-severity findings: 1

## Repair population

Commit e7ad7934 over the round-6 reviewed commit 8a0bb2a1, restricted to this
package (without its reviews folder) and the builder: 20 insertions and 13
deletions in 3 files (the packet, the semantic delta, the builder). The four
patches and the four manifest rows are unchanged: the manifest file digest is
the same before and after.

## Dispositions

### R6-1 — "mapped whatever its stem" ignored the suffix condition (revise)

Repaired in the builder's generated block. The clause now reads "a file
directly inside a top-level licenses folder and ending .md or .txt is mapped
whatever its stem unless a word above withholds it", with the suffixes taken
from the constant. licenses/LICENSE, licenses/COPYING, licenses/README and
licenses/README.rst are withheld fixtures (they lack .md or .txt), and the
below-the-root predicate checks them and the suffix text.

### R6-2 — the licenses half of the example guard was unguarded (note)

Repaired. The guard uses sub/Guide, mapped in docs and withheld in licenses
(depth three), and `examples_hold` takes the roots to test. The surviving
mutant that dropped the licenses root now fails the selftest.

### R6-3 — tree names matched by substring (note)

Repaired. The predicate matches whole words, so "doc" no longer matches
"docs". A mutant that names only the docs tree fails the selftest.

### R6-4 — the packet described the recorder as unwritten (note)

Repaired. The packet says a recorder, frozen only after a confirming review,
takes the chosen row, and that the recorder refuses a second variant act over
this manifest unless it is a declared superseding version.
