# Round 5 dispositions — public-source screening scope, version 2

> **Candidate — binds nothing.** Record for
> `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-5-RAW.md` (verdict REVISE;
> finding R5-1 revise, R5-2 to R5-4 notes), written 2026-10-04. The raw is
> retained verbatim. No digest is copied here.

## Why there was a round 5

`ROUND-4-DISPOSITIONS.md` says there would be no round 5, and that sentence is
left as it stood because a raw reviewed it. The lead then chose to dispatch one
narrow round over the round-4 repair: recording the package over unreviewed
bytes would have weakened the recorder's gate and needs an owner act, so the
recorder accepts only a confirming review (CONFIRM, or notes-only CONFIRM WITH
EXCEPTIONS) and the repair needed reading. This record supersedes that
sentence. Round 6, scoped strictly to the diff below, is the last round: if it
does not confirm, the recorder stays unfrozen and the owner chooses.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-source-screening-scope-v2/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-5-RAW.md
Revise-severity findings: 1

## Repair population

Commit 39d83718 over the round-5 reviewed commit fd4e2509, restricted to this
package (without its reviews folder) and the builder: 77 insertions and 37
deletions in 9 files. The same commit also removes the recorder's second review
form and unfreezes the recorder (outside the reviewed paths), and leaves the
installer and simulator changes in place.

## Dispositions

### R5-1 — the withheld-READMEs wording contradicted the licenses mapping (revise)

Repaired in the builder. The generated line now names the trees the exception
covers: READMEs and other root names below the root outside docs, doc and
licenses are withheld, and a file directly inside a top-level licenses folder is
mapped whatever its stem unless a listed word withholds it. The policy's
`notMapped` says "outside docs-tree and licenses-tree", and `indeterminate`
gives src/README.md as its example. A selftest predicate ties the line to
fixtures (licenses/README.md, LICENSE.txt, CHANGELOG.md and NEWS.md mapped;
src/README.md and src/NEWS.md withheld) and to the generated text. All four
manifest rows changed.

### R5-2 — the variant line and notMapped described the word list as docs-only (note)

Repaired in the same regeneration: each variant line now says it lifts the word
from the docs and licenses withholding, and `notMapped` says "docs-tree and
licenses-tree paths whose directory or file name has a word".

### R5-3 — the example predicate tested literals; the sentence overstated (note)

Repaired. The example names are one constant read by the sentence and by the
predicate, which checks each in both the docs and the licenses tree. Two new
mutants fail: a falsified example (Security) and an example withheld in
licenses. The sentence now says text under any other name "inside the mapped
paths" is sendable, so policy files under src stay withheld.

### R5-4 — the review brief was the round-4 brief (note)

Repaired. The brief is the round-6 brief with criterion 12 for the round-5
diff, criterion 1 corrected (the variants also differ in the opt-in words in
`docExcludedTokens` and in the `policyVersion` suffix), and the recording name
for the round-6 raw.
