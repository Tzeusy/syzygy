# Round 4 dispositions — public-source screening scope, version 2

> **Candidate — binds nothing.** Record for
> `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-4-RAW.md` (verdict REVISE;
> finding B-1 blocking, N-1 to N-4 notes), written 2026-10-04. The raw is
> retained verbatim. Round 4 is the stopping round under the agreed rule
> (repair, dispatch nothing, ask the owner): there is no round 5. No digest is
> copied here.

## Unreviewed repair

Repaired after the final (4th) review round. This delta, 70 insertions and 28
deletions in 8 files (commit 33b15a65 over the reviewed commit 72ddd762: the owner
packet, the semantic delta, the manifest, four patches and the builder; it
excludes the retained raw, this file and the statement in the packet), is
unreviewed. The owner may sign the reviewed state at 72ddd762 plus this delta,
or ask for one more review. Population: `git diff --stat 72ddd762..33b15a65`.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-source-screening-scope-v2/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-4-RAW.md
Revise-severity findings: 1

## Dispositions

### B-1 — Q1 and the scope sentence overclaimed for the licenses folder (blocking)

Repaired by tightening the rule, not the wording. The licenses-tree path rule
now takes the same whole-word denylist as the docs tree, applied to the file
name without its extension, and the opt-in words are denied there unless the
variant adds them. licenses/SECURITY.md, licenses/governance-policy.md,
licenses/CODE_OF_CONDUCT.md, licenses/doctrine.txt and, in variant none,
licenses/MANIFESTO.md and LICENSES/Architecture.txt are now withheld; fixtures
cover each, licenses/agpl-3.0.txt, licenses/README.md and
licenses/SecurityPolicy.md stay mapped, and a mutant without the licenses
denylist fails the selftest. Q1 and the generated lists now name the licenses
folder as a place the rule looks. Selftest: 112 of 112.

### N-1 — The scope sentence was a literal nothing checked against the rule (note)

Repaired. The sentence is built from the rule's constants (denylist words,
opt-in words, withheld root names, docs and licenses roots). New selftest
predicates check that it names every one of them, that it is inside the
generated block, that its two named examples are mapped by the rule, and that
dropping a denylist word changes it.

### N-2 — Q4's default overstated (note)

Repaired. Q4's default now names what is mapped: the root README, a README
under docs or doc, and a README directly under licenses; a README elsewhere is
withheld.

### N-3 — Q3's word list omitted doctrine and principle (note)

Repaired. Q3 lists doctrine and principle, and says the same words withhold a
file name directly under the licenses folder.

### N-4 — The requested diff range carried main-side files (note)

No repair; the reviewer reviewed the PR's paths. The repair diff above is
stated by commit range.
