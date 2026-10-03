# R-RFC5-PROJECT-DOCUMENTATION-CLASS — fresh-context review, round 1
Reviewed commit: 5c820b2e85caf95d06d5bd0ce1167ae91a3ebe22
Manifest SHA-256: 8c643089fe95fed706a11fc310d291f4b5834a4ec44faf0a05e720451f7583fa
Verdict: REVISE

Subject package: `.syzygy/governance/contracts/candidates/rfc5-project-documentation-class/`
(all six files) and `scripts/build_rfc5_project_documentation_class.py`, read
in a detached worktree at the reviewed commit. The manifest digest above was
printed by `sha256sum` over the manifest file at that commit. Reviewer: a
fresh-context agent that did not draft the package and did not share its
session. Read: the brief's artifacts and governing references, AGENTS.md
verification rules, and (for criterion 10) the Scope A direction and the
2026-10-02 re-pin instructions the packet cites.

## Checks run

- [Observed] `python3 scripts/build_rfc5_project_documentation_class.py --check`:
  exit 0, "manifest matches the patched module on both identical mirrors; …
  verify_final_prespec, CG-13 and CG-17 pass".
- [Observed] `--selftest`: "14 fixtures, 0 failing", exit 0.
- [Observed] Independent re-derivation: the installed and candidate mirrors
  are byte-identical (`cmp`); GNU `patch -p1` applies the package patch
  cleanly to a copy; the result hashes (`sha256sum`) to the manifest's one
  row; `diff` against the current module shows 16 added lines and 0 removed
  lines (1 table row + 15 bullet lines). Nothing outside RFC5-14 changes.
- [Observed] Own mutants against `check()` on a fixture root (rule 6):
  dropping the consent sub-bullet from the patch → "manifest differs from
  exact regeneration"; an extra `.patch` file → "patch(es) outside the
  one-module population"; a duplicated composite-style bullet → manifest
  mismatch; a front-matter line added → "front matter changed". Restored
  fixture verifies clean.
- [Observed] Impact sweeps re-run with Python `re` over `git ls-tree -r -z`
  at `dbf8ed1911aa193b0db7cfebdf8d4338c7500ba0` (the reviewed commit's
  parent): 1973 tracked files, 4 not UTF-8; A = 78; B = **82**; A∩B = 20;
  A∪B = **140**; C = 7. See Finding 2.
- [Observed] `SOURCE-POLICY.md`'s current sha256 appears in
  `decisions/ACCEPTANCE-ACT-RECORD.md` (line 778),
  `decisions/POLARIS-GENERATOR-BASE-READABILITY-SUCCESSOR-ACT.md` and the
  base readability successor's `SUCCESSOR-MANIFEST.txt`: it is bound by a
  performed act and correctly left unedited.
- [Observed] No standalone 64-hex token in any of the four package Markdown
  files; each opens "**Candidate — binds nothing.**". The words accepted /
  adopted / sign-off occur only about other artifacts (the accepted module,
  the adopted generator specification, the Scope A sign-off mechanism) or in
  the brief's own criterion text; nothing in the package is labelled
  accepted, adopted, approved or signed off.
- [Observed] Warrant: on `origin/polaris/public-repo-admission`
  (`1082959`…, PR 215), `decisions/PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md`
  records Q7 answered "Amend RFC5-14; T1 starts without (Recommended)", and
  direction item 3 says the amendment "is drafted as its own candidate
  package with its own act". The delta's warrant matches.

## Criteria

1. **Change class.** Normative is right overall: a new consentable class is a
   widened possibility under RFC5-15's "within the consented set". SEC-2
   (`doctrine/security.md` lines 42–54) requires consent to "name … the content
   classes" but enumerates none, so no doctrine act is needed. Parts of the
   bullet are Clarifying restatements (docstrings inside source are
   `code-content`; a consent not listing a class does not permit it — already
   RFC5-15 part 2). One sentence is Normative in a way the delta does not
   disclose: Finding 1.
2. **Patch scope.** Yes. One row and one bullet, pure insertion; six rows,
   composite bullet, clause leads, front matter and headings byte-identical
   (builder and independent diff agree).
3. **Membership.** Placement of the ten samples, without the fail-closed rule:
   README → `project-documentation`; CONTRIBUTING → listed, but see Finding 5;
   LICENSE → listed ("licence and notice files"); architecture overview →
   **ambiguous** ("overview documents" vs. design text as `governance-text`);
   design decision record → `governance-text` ("decision"); specification →
   `governance-text`; docstring-heavy source → `code-content` (explicit);
   changelog → listed; generated API reference → **ambiguous**; notebook →
   **ambiguous** (code cells are `code-content`, prose cells are
   documentation; "exactly one class" fails, so it fails closed). Finding 5.
4. **Consent widening.** No. RFC5-15 part 2 requires the class "within the
   consented set"; the new third sub-bullet restates that and adds that no
   pre-existing consent covers the new class. No conflict found with RFC5-14's
   other bullets, RFC5-15 or the composite rule.
5. **Composite rule and screening.** True of the proposed text: the composite
   bullet is byte-identical and the new bullet defines no order. "rule above"
   resolves to the composite bullet immediately preceding it. "as below"
   resolves only loosely: Finding 6.
6. **Blast radius.** A, C and the group arithmetic reproduce; B and the union
   do not: Finding 2. Rule 9 sweep for unlisted enumerations, also over
   underscore/space/CamelCase spellings across doctrine, decisions, policies,
   openspec, scripts, apps, packages and installed rfcs (1976 of 1980
   readable files at the reviewed commit): no further authority text
   enumerates the vocabulary. SEC-2 and `craft-and-care/security-and-secrets.md`
   list "source structure, specs, work history" as what is *covered*, which is
   not the vocabulary. The 20 code files use only the string `code-structure`
   (a POC module and adapter name). Off `main`, the PR 215 egress record
   (five classes) is affected and the packet says so.
7. **Migration.** Correct that the patch must not be applied while a
   candidate (CG-7h binds the path; the restyle manifest binds the current
   bytes). The plan names manifest regeneration, CG-7h/contract-index
   regeneration and a fresh digest-binding review (workflow rule 7). The
   `SOURCE-POLICY.md` step is weaker than workflow step 6: Finding 3.
8. **Verification.** `--check` and `--selftest` pass and the mutants I added
   fail as they should. Uncovered claims: Finding 7.
9. **Authority claims.** None found (see Checks run).
10. **Act form.** Option 3's reading of Scope A is accurate and labelled
    [Inferred]; Scope A item 1 names "the PWB specification deltas, the
    observer registry entry and the contract successors queued behind them",
    and its closing paragraph keeps phrase-and-digest acts as the only route
    for queued packages until the replacement change lands. Option 1's
    precedent is described accurately. One inconsistency about which digest
    binds: Finding 4.

## Findings

**Finding 1 — "a file extension, a directory name or a file's own claim about itself places nothing" constrains classification-policy content, contradicts "decided by the declared policy", and is undisclosed** (blocking)
`proposed/RFC-0005/consent-egress-secrets.md.patch:23-24`; `SEMANTIC-DELTA.md:58-59`.
The new bullet's lead says membership is "decided by the declared policy, per
file", and the delta's Proposed meaning (lines 67–72) says "the declared policy
decides". The appended clause then says extension, directory name or
self-claim "places nothing", without restricting it to the absence of a
policy rule. Read literally it forbids a declared policy whose rules key on
path or extension (`docs/**`, `LICENSE*`, `*.md`), which is the ordinary
way such a policy is written ([Inferred] from AGENTS.md's note that PWB
Phase B classifies baseline specs path-only). That is a new constraint on classification-policy
*content*, which `rfcs/RFC-0005/README.md:182` lists under "Not this RFC's";
the delta's "What explicitly does NOT change" and Change class lines (9,
74–92) do not name it, so the class claim is incomplete (template Rules on the
classes 1–2; NORMATIVE-CHANGE-WORKFLOW step 1). It is also ambiguous whether
it reaches all seven classes or only this one, since it sits under the
`project-documentation` bullet but speaks of "a file". Repair: say what is
meant, e.g. that such signals place a file only through a rule of the
declared policy, never on their own; or drop the clause and leave the
untrusted-self-claim point to RFC3-16(a) and the policy; and record the
choice in the delta.

**Finding 2 — Sweep B and the union do not reproduce from the printed predicate** (blocking)
`IMPACT-LEDGER.md:15`, `:18`, `:30`, `:37`; `SEMANTIC-DELTA.md:122-125`.
Brief criterion 6; AGENTS.md verification rules 2, 3 and 9. Running regex B as
printed, "counted when 14 is a listed number or lies inside a
`..`/`…`/`–` range", at `dbf8ed19…` gives 82 files, A∪B = 140, A∩B = 20.
A variant that counts any match whose minimum-to-maximum span contains 14
when the match holds a range separator gives exactly 83, and its one extra
file is `.syzygy/governance/contracts/candidates/round-2026-08c/reviews/RD-8-exact-manifest-RAW.md`
("RFC5-1..RFC5-11, RFC5-24..RFC5-26"), which excludes 14 under the stated
rule. [Inferred] that is the drafter's extra file; my own grouping gives 23
round-* files where the ledger says 24, consistent with it. A, C and the
other group counts reproduce. The conclusions do not change (that file is a
round raw, never edited), but the figures and the "24 round-*" cell are
wrong as published and "= 141" sums a population the predicate does not
produce. Repair: publish the counting rule actually run, or recount under
the printed one; correct B, the union and the rounds cell in both files.

**Finding 3 — The `SOURCE-POLICY.md` step defers propagation the workflow requires in the same change** (note)
`SEMANTIC-DELTA.md:145-150`; `OWNER-DECISION-PACKET.md:74-78`.
NORMATIVE-CHANGE-WORKFLOW step 6: "Every invalidated authoritative artifact is
updated in the same change … an open follow-up is syncing later by another
name." `SOURCE-POLICY.md:26-27` says in the present tense that "The egress
vocabulary remains" the six; after adoption that is false on a default
reading path of an adopted change. Surfacing it to the owner satisfies
template rule 6, and the file cannot be edited, but option "leave it
disclosed as historical" names no place where the disclosure would be made,
and the delta's gloss ("reads as describing the six classes the spec was
adopted against") is a reinterpretation of "remains" the bound text does not
support. Suggest the plan name the readability successor as the step-6
propagation, or say where the disclosure lives and that it departs from
step 6.

**Finding 4 — The packet says the act binds the manifest file's digest, while its recommended form binds the manifest row** (note)
`OWNER-DECISION-PACKET.md:50` vs `:52-55`; `CONTRACT-AMENDMENT-MANIFEST.txt:4-5`.
The manifest header says its rows bind "by the owner act that names this
file's digest"; the packet line 50 agrees. Option 1, per the 2026-10-02 re-pin
(`decisions/OWNER-INSTRUCTIONS-2026-10-02-PWB-BEHAVIOR-CONTRACT-REPIN.md`:
"each act's argument is that subject's row"), binds the row, a different
digest for this one-row manifest. AGENTS.md's recorder note ("Say which
digest the raw's head must carry") records the cost of leaving this implicit.
Suggest the packet state which argument each option binds.

**Finding 5 — Membership is ambiguous for four of the ten samples, and "contribution guides" sits in tension with "does not govern its development"** (note)
`proposed/RFC-0005/consent-egress-secrets.md.patch:8`; `SEMANTIC-DELTA.md:67-72`.
Brief criterion 3. Ambiguous without the fail-closed rule: architecture
overview ("overview documents" here; the Q2 answer on PR 215 maps "design
docs" to `governance-text`); generated API reference (built from docstrings
the same bullet makes `code-content` when inside source, so a policy placing
it here lets docstring text egress under a consent that excludes
`code-content`; the declared-policy act is the guard, which is acceptable but
worth one sentence); notebook (mixed; fails closed); and CONTRIBUTING or
developer guides that state binding process rules (DCO, review requirements),
which the enumeration places here while the definition excludes text that
governs development. The sub-bullet's policy-decides rule resolves each, so
"contribution guides" is not wrong, but the row asserts membership the
definition does not secure. Suggest qualifying the enumeration ("ordinarily")
or naming the policy as the tie-breaker in the row's terms.

**Finding 6 — "as below" points at a paragraph about composites** (note)
`proposed/RFC-0005/consent-egress-secrets.md.patch:23`; module `consent-egress-secrets.md:162`, `:169`, `:188`, `:254`.
The paragraph below ("Classification is determinable, provenance-tracked,
and fails closed") states the fail-closed rule for "A composite whose class
cannot be determined". A single undeterminable file fails closed by RFC5-15
part 2 ("determinable and within the consented set") and RFC5-16 ("cannot be
classified is excluded"). The reference resolves by analogy only; citing
RFC5-15 would resolve it exactly.

**Finding 7 — Builder claims no selftest mutant covers** (note)
`scripts/build_rfc5_project_documentation_class.py:26-36`, `:287-290`, `:331-334`.
Rule 6. No selftest fixture exercises: a CG-13 or CG-17 failure on the
scratch tree (only `verify_final_prespec` is mutated, line 304), though
`--check` prints that CG-13 and CG-17 pass; a clause-lead change; a
front-matter change (I confirmed by hand it is caught); a patch file outside
the population (confirmed caught by hand); "patch changes nothing"; the two
mirrors patching to different bytes; and the `applied()` path. The
"misplaced" mutant's middle `.replace("| `derived-composites`", "| `derived-composites`", 1)`
is a no-op. The delta's line 89–90 also says "the builder verifies all
three" after listing four items.

**Finding 8 — The quoted current meaning is not the bootstrap-bound bytes** (note)
`SEMANTIC-DELTA.md:15`.
"quoted from the module at the digest the bootstrap manifest binds". The
general trusted-bootstrap manifest row for the module
(`general-trusted-bootstrap-authorization/CONTRACT-AMENDMENT-MANIFEST.txt:22`)
hashes commit `92cfbf3e`'s bytes, where the composite rule is a run-on prose
paragraph; the quote's bullet form is the current, restyle-bound bytes
(hash present in `contract-readability-restyle/CONTRACT-AMENDMENT-MANIFEST.txt`
and `ACTIVE-CONTRACT-MANIFEST.txt`). Wording is the same; the provenance
statement is not. Suggest "at its current bytes, which the readability
restyle binds".

## Summary

Two blocking findings (1, 2) and six notes. The patch is mechanically exact,
widens no consent, keeps the composite rule and RFC5-16 screening intact, and
claims no authority. Finding 1 is a normative ambiguity in the proposed
contract text; Finding 2 is a published figure that does not reproduce from
its own predicate.
