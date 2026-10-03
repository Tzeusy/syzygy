> **Candidate — binds nothing.** Dispositions of the round-1 findings on this
> package. It is not a review, carries no verdict and confirms nothing; a
> later round decides whether each disposition is true of the bytes it names.

# Round-1 dispositions — RFC5-14 `project-documentation` class

Reviewed record: `reviews/R-RFC5-PROJECT-DOCUMENTATION-CLASS-1-RAW.md`
(verdict of record: REVISE; reviewed commit 5c820b2e85caf95d06d5bd0ce1167ae91a3ebe22).
The raw is retained verbatim and not edited.

Every count below was re-derived by script from the repaired bytes or the
named commit, not copied from the raw.

| # | Class | Disposition | Where |
|---|---|---|---|
| 1 | blocking | Repaired by narrowing, disclosed | patch; `SEMANTIC-DELTA.md` |
| 2 | blocking | Repaired: rule published, every figure re-derived | `IMPACT-LEDGER.md`; `SEMANTIC-DELTA.md` |
| 3 | note | Accepted; propagation path named | `SEMANTIC-DELTA.md` migration step 2; packet |
| 4 | note | Accepted | `OWNER-DECISION-PACKET.md` |
| 5 | note | Accepted | patch table row; `SEMANTIC-DELTA.md` |
| 6 | note | Accepted | patch |
| 7 | note | Partly accepted | builder |
| 8 | note | Accepted | `SEMANTIC-DELTA.md` |

## Finding 1 — signals clause

The reviewer's reading is right: "places nothing" was unqualified and read as
forbidding a declared-policy rule keyed on path or extension, which RFC-0005
README line 182 lists as "Not this RFC's". **Narrowed, not removed.** The
sub-bullet now says such a signal places a file in this class "only through a
rule of the declared policy, never on its own", and scopes itself to this
class. The untrusted-claim point stays because it is RFC3-16(a)'s point and
costs nothing; the clause no longer says anything about what a policy may
contain. `SEMANTIC-DELTA.md` discloses the change in three places: the
proposed bullet, a paragraph explaining what the sub-bullet says and does not
say, and a new "does NOT change" line naming classification-policy content.
The patch hunk header was updated (21 to 22 added lines) and the manifest
regenerated; the builder's `--check` confirms the patched module.

## Finding 2 — sweep B and the union

Reproduced. My own script (the run form as printed, then the span rule below)
gives, at `dbf8ed19` and at the `origin/main` this round is rebased on
(`9a6e8e31`): A = 78, B = 82, A and B together 20, union = 140, C = 7, the
same at both commits. The round-1 figures B = 83 and union = 141 are not
produced by the printed rule; the extra file is the `round-2026-08c` raw the
reviewer named, which the printed rule excludes (its pairs are 1..11, 11-24
and 24..26, none containing 14). I do not know how round 1's 83 was produced
and do not assert it. The ledger now publishes the run form, the pair-reading
rule, the line-break handling and the group path rules, restates the
denominator for `9a6e8e31` (1988 files, 4 not UTF-8), and regroups the union
by a stated path prefix in order; the group counts are mine, not the
reviewer's, and the rounds cell is 23. The delta's Downstream impact section
carries the new figures. The ledger's conclusions are unchanged.

## Finding 3 — SOURCE-POLICY.md step

Accepted. The delta now names a readability successor as the only lawful
step-6 propagation, says the delta departs from step 6 if the owner leaves
the file as is, says where that disclosure lives, and drops the reading of
"remains" the bound text does not support. The packet's consequence section
says the same to the owner in plain terms. The package does not choose.

## Finding 4 — which digest an act binds

Accepted. The packet states that option 1 binds the manifest row, option 2
the manifest file, and option 3 neither, and that the two digests differ for
this one-row manifest. The brief says the raw's head carries the file digest.

## Finding 5 — membership

Accepted. The table row now ends "ordinarily; the declared policy decides each
file", naming the policy as tie-breaker in the row's own terms. The delta
adds a paragraph on the four kinds of file the list does not settle
(architecture overview, a contribution guide with binding rules, a generated
API reference, a notebook), including the one-sentence docstring-egress
point on generated references.

## Finding 6 — "as below"

Accepted. The patch now cites RFC5-15 ("fails closed (RFC5-15)"), whose part 2
requires a determinable class within the consented set.

## Finding 7 — builder coverage

Partly accepted. Added fixtures: clause-lead change, front-matter change, a
patch outside the one-module population, a patch that changes nothing, and
both arms of `applied()`. Removed the no-op `.replace`. Adding the
clause-lead fixture exposed a real defect: `_table_rows` raised `ValueError`
when the lead was altered, instead of reporting; it now returns no rows and
the structure check reports the finding. The delta's "all three" now names the
three things the builder verifies. **Not covered, disclosed:** a CG-13 or
CG-17 failure on the scratch tree is not mutated (only
`verify_final_prespec` is), and the two-mirrors-patch-differently branch is
unreachable while the mirror-drift check runs first; `--check`'s message still
says CG-13 and CG-17 pass, which is true of the run and unproved by a mutant.

## Finding 8 — provenance of the quoted meaning

Accepted. The delta now reads "at its current bytes, which the contract
readability restyle binds". I did not re-read the bootstrap manifest row.
