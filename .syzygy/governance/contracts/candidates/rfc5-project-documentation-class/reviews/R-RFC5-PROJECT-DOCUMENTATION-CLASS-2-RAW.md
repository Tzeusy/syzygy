# R-RFC5-PROJECT-DOCUMENTATION-CLASS — fresh-context review, round 2
Reviewed commit: dff2f0dc5cf6b8a876c4d4233cb0bef8e3e7dce4
Manifest SHA-256: 361d1948fb7c3e06a0fbb9cae71e5ecdaabfaefb45cb29531b8d4bfd2135cb6f
Verdict: CONFIRM WITH EXCEPTIONS

Subject package: `.syzygy/governance/contracts/candidates/rfc5-project-documentation-class/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `REVIEW-BRIEF.md`,
`OWNER-DECISION-PACKET.md`, `CONTRACT-AMENDMENT-MANIFEST.txt`,
`proposed/RFC-0005/consent-egress-secrets.md.patch`, and `reviews/`) and
`scripts/build_rfc5_project_documentation_class.py`, read in a detached
worktree at the reviewed commit. The manifest digest in the head was printed by
`sha256sum` over the manifest FILE at that commit. Reviewer: a fresh-context
agent that did not draft the package, did not share its session, and did not
write round 1. Read: the brief, its governing references, the round-1 raw and
`reviews/ROUND-1-DISPOSITIONS.md`, and AGENTS.md's verification rules.

## Checks run

- [Observed] `python3 scripts/build_rfc5_project_documentation_class.py --check`:
  exit 0, "RFC-0005 project-documentation manifest matches the patched module
  on both identical mirrors; clause leads, front matter and headings
  unchanged; the six existing RFC5-14 rows and the composite bullet are
  byte-identical; verify_final_prespec, CG-13 and CG-17 pass".
- [Observed] `--selftest`: "20 fixtures, 0 failing", exit 0.
- [Observed] Independent re-derivation: installed and candidate mirrors are
  byte-identical (`cmp`); GNU `patch -p1` applies the package patch cleanly to
  a copy; `sha256sum` of the result equals the manifest's one row
  (`a69a606c…`, row of the manifest, not the file digest); `diff` shows 17
  added and 0 removed lines (1 table row + 16 bullet lines), all inside RFC5-14.
  The current module hashes to the row that `contract-readability-restyle/CONTRACT-AMENDMENT-MANIFEST.txt:27`
  and `ACTIVE-CONTRACT-MANIFEST.txt:22` carry; the bootstrap manifest row
  (`general-trusted-bootstrap-authorization/CONTRACT-AMENDMENT-MANIFEST.txt:22`)
  names the module at earlier bytes. Both bindings stand; the patch is
  correctly unapplied.
- [Observed] Own mutants against `check()` on a fixture root (rule 6):
  clause lead `**RFC5-14.**` → `**RFC5-14**` gives "clause leads changed: lost
  ['RFC5-14']" (plus two table findings); changing "fails closed (RFC5-15)",
  weakening the consent sub-bullet, and dropping the RFC5-16 screening clause
  each give "manifest differs from exact regeneration over the proposed
  bytes"; a patch header naming `rfcs/RFC-0005/README.md` gives "touches
  ['rfcs/RFC-0005/README.md'], expected exactly …" on both mirrors. Restored
  fixture verifies with no finding.
- [Observed] `python3 scripts/check_governance.py` at the reviewed commit:
  "31 OK, 21 WARN, 0 FAIL (52 checks)".
- [Observed] Impact sweeps re-run by my own script (Python `re`, case-sensitive,
  over `git ls-tree -r -z` blobs read by `git cat-file --batch`), regexes, run
  form and span rule as printed at `IMPACT-LEDGER.md:13-29`:
  - at `9a6e8e31cfa842e83fa0970765f581579b40de3b`: 1988 tracked files, 4 not
    UTF-8; A = 78, B = 82, A∩B = 20, A∪B = 140, C = 7;
  - at `dbf8ed1911aa193b0db7cfebdf8d4338c7500ba0`: 1973 files, 4 not UTF-8;
    A = 78, B = 82, A∩B = 20, A∪B = 140, C = 7;
  - the min-to-max variant the ledger describes at line 27-29 gives B = 83 at
    both, the one extra file being
    `.syzygy/governance/contracts/candidates/round-2026-08c/reviews/RD-8-exact-manifest-RAW.md`,
    exactly as the ledger says;
  - second method (rule 2): `git grep -lP` for A at `9a6e8e31` gives 78; a
    literal `RFC5-14(?!\d)` grep gives 73, the remaining 9 of B coming from
    lists and ranges, consistent with the span rule;
  - groups by first matching prefix in the ledger's order (`IMPACT-LEDGER.md:39-59`):
    installed 9, mirror 15, restyle 9, history 6, rounds 23, raws 14,
    evidence 10, pursuits 4, openspec 9, code 20, docs 6, decisions 1,
    generated 1, other `.syzygy/` 13, unmatched 0 — sum 140, identical to the
    ledger at both commits. All 20 code files name only `code-structure`.
  - C's seven files: both RFC-0005 mirrors, the restyle patch, one `history/`
    RFC, two `docs/evidence/` JSON records and `SOURCE-POLICY.md`. Of these
    only `SOURCE-POLICY.md` is authority text other than the subject.
- [Observed] Rule-9 sweep for an unlisted enumeration: every tracked UTF-8
  file at the reviewed commit, each class name matched case-insensitively with
  `-`, `_`, space or nothing between its words (so `governanceText`,
  `code_content`, "work history" count), threshold two names, outside the
  round, history, review-raw, evidence and pursuit trees: 16 files. Beyond the
  subject, its mirror, this package, its builder and the restyle patch, they
  are `SOURCE-POLICY.md` (6 names), REQ-025's spec (2), `three-surface-poc-experience/CONTRACT-COVERAGE.md`
  (2), two docs notes (2 and 3) and two D6 doctrine-review raws (2). None of
  the latter enumerates the vocabulary. No authority text the ledger omits.
- [Observed] `SOURCE-POLICY.md`'s current sha256 appears in
  `decisions/ACCEPTANCE-ACT-RECORD.md:778`,
  `decisions/POLARIS-GENERATOR-BASE-READABILITY-SUCCESSOR-ACT.md` and
  `polaris-generator-base-readability-successor/SUCCESSOR.json`: bound by a
  performed act and correctly left unedited. Its line 26 reads "The egress
  vocabulary remains governance-text, code-structure, code-content,
  work-history, evidence-content and derived-composites."
- [Observed] Warrant: on `origin/polaris/public-repo-admission`
  (`7704b4a5…`), `decisions/PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md:31`
  records Q7 answered "Amend RFC5-14; T1 starts without (Recommended)". The
  delta's warrant matches.
- [Observed] Package Markdown: every non-raw file opens "**Candidate — binds
  nothing.**"; 0 standalone 64-hex tokens in `SEMANTIC-DELTA.md`,
  `IMPACT-LEDGER.md`, `REVIEW-BRIEF.md`, `OWNER-DECISION-PACKET.md` and
  `ROUND-1-DISPOSITIONS.md`; 1 in the round-1 raw (its required head line).
  "accepted", "adopted" and "sign-off" occur only about other artifacts (the
  accepted module, the adopted generator specification, the Scope A
  mechanism, a successor's sign-off) or in the brief's criterion text.

## Criteria

1. **Change class.** Normative is right: a new class makes consentable what
   RFC5-15 part 2 ("determinable and within the consented set") refused. SEC-2
   (`doctrine/security.md:42-56`) requires consent to name "the content
   classes they may receive" but enumerates none, so no doctrine act is
   needed. Several sub-bullet sentences are Clarifying restatements
   (fail-closed on an undeterminable file is RFC5-15 part 2; a consent not
   listing a class does not permit it). No undisclosed Normative sentence
   remains of the kind round 1 found; see Finding 1 for one residual scope
   question.
2. **Patch scope.** Yes. One row, one bullet with four sub-bullets, pure
   insertion; builder and my own diff agree; mutants confirm the builder
   rejects edits to rows, the composite bullet, clause leads, front matter and
   headings.
3. **Membership.** Placement of the ten samples, without the fail-closed
   rule: README → `project-documentation`; CONTRIBUTING →
   `project-documentation` "ordinarily", `governance-text` where it sets
   binding rules (the row's "does not govern its development" plus the policy
   tie-breaker now handles this; "contribution guides" no longer sits wrongly);
   LICENSE → `project-documentation` ("licence and notice files");
   architecture overview → ambiguous, policy decides; design decision record →
   `governance-text`; specification → `governance-text`; docstring-heavy
   source → `code-content` (explicit); changelog → `project-documentation`;
   generated API reference → ambiguous, policy decides (the delta's warning at
   `SEMANTIC-DELTA.md:84-88` is accurate; [Inferred] RFC5-14's existing
   provenance clause, "tracked from where the content originated", is a second
   guard where the origin is known); notebook → ambiguous, see Finding 1.
4. **Consent widening.** No. RFC5-15 part 2 requires the class "within the
   consented set"; the third sub-bullet restates that and adds that no
   earlier consent covers the new class. No conflict with RFC5-14's other
   bullets, RFC5-15 or the composite rule.
5. **Composite rule and screening.** True. The composite bullet is
   byte-identical (builder, mutant, diff); the new bullet defines no order;
   "rule above" resolves to the composite bullet directly preceding it;
   "fails closed (RFC5-15)" now cites a clause that states it for any content:
   RFC5-15 part 2, "(RFC5-14 — undeterminable fails closed …)" (module lines
   188-192). RFC5-16 ("content that **cannot be classified is excluded, not
   indexed**", line 253-254) is unchanged and the bullet says it applies in
   full.
6. **Blast radius.** Every figure reproduces at the named commit and at the
   round-1 commit (Checks run). The ledger's explanation of round 1's 83/141
   is correct. No unlisted authority enumeration. `SOURCE-POLICY.md` is bound
   and correctly unedited.
7. **Migration.** Correct that the patch must not be applied while a
   candidate (the restyle and active manifests bind the current bytes; the
   bootstrap manifest binds the path under CG-7h). Step 1 names manifest
   regeneration, CG-7h and contract-index regeneration and a fresh
   digest-binding review (workflow rule 7). Step 2 now names the readability
   successor as the only lawful step-6 propagation, discloses the departure if
   the owner declines it, and leaves the choice to the owner. Sound.
8. **Verification.** `--check` and `--selftest` pass and my mutants fail as
   they should. Claims no mutant covers: CG-13 and CG-17 failures on the
   scratch tree, and the mirrors-patch-differently branch (unreachable while
   the drift check runs first); both disclosed at `ROUND-1-DISPOSITIONS.md`
   Finding 7. The bullet's text beyond "no ordering among classes" is guarded
   only by the manifest regeneration, which is the act argument and suffices.
9. **Authority claims.** None found. The round-1 raw's head digest is the only
   64-hex token in package Markdown; see Finding 3.
10. **Act form.** Accurate. Option 3's reading of Scope A is labelled
    [Inferred]; Scope A (`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md:30-32`)
    names "the PWB specification deltas, the observer registry entry and the
    contract successors queued behind them", which does not obviously reach
    this amendment. The packet now states which digest each option binds. One
    residual: Finding 2.
11. **Round-1 repairs.** Finding 1 — resolved in substance: the signals
    sub-bullet now reads "places a file in this class only through a rule of
    the declared policy, never on its own", which constrains only how a signal
    places a file in this class, and `SEMANTIC-DELTA.md:93-100` and `:113-116`
    say so; the scope half of round-1 Finding 1 is only partly addressed
    (Finding 1 below). Finding 2 — resolved: the published predicate and my
    own run agree on every figure. Findings 3, 5, 6, 7, 8 — dispositions true
    of the current bytes. Finding 4 — true of the packet; the manifest header
    still says otherwise (Finding 2 below).

## Findings

**Finding 1 — "exactly one class" is not scoped to this class, and the delta's notebook account omits the composite route** (note)
`proposed/RFC-0005/consent-egress-secrets.md.patch:22-23`; `SEMANTIC-DELTA.md:89-91`; `reviews/ROUND-1-DISPOSITIONS.md:31-32`.
Round 1 Finding 1 also asked whether the sub-bullet "reaches all seven classes
or only this one". The disposition says the sub-bullet "scopes itself to this
class"; that is true of its second half ("places a file in this class") but
not of its first: "A file the policy cannot place in exactly one class is
undeterminable and fails closed (RFC5-15)" speaks of any file. [Inferred] Read
generally it is a Clarifying restatement of RFC5-15 part 2 and the composite
rule (a policy either derives one class, the highest embedded, or the class is
undeterminable), so no consent widens and nothing conflicts. But the delta's
notebook paragraph says a notebook "is not placed in exactly one class, so it
is undeterminable and fails closed unless the policy splits it"; under the
unchanged composite rule a policy may equally place the whole notebook in its
highest embedded class (for example `code-content`) as one class, which
neither splits it nor fails closed. Suggest "unless the policy splits it or
places it whole" in the delta, and either scope the sentence ("… in exactly one
class, this one included, …") or record in the delta that it restates RFC5-15
for every class. Not blocking: no reading changes what is consentable.

**Finding 2 — The manifest header says the act names the file's digest; the packet's recommended option binds the row** (note)
`CONTRACT-AMENDMENT-MANIFEST.txt:4-5` (rendered by `scripts/build_rfc5_project_documentation_class.py:118-119`); `OWNER-DECISION-PACKET.md:50-69`.
The packet now says option 1 binds the manifest row and option 2 the file,
which repairs round-1 Finding 4 there. The manifest's own header still reads
"These rows bind only by the owner act that names this file's digest in
ACCEPTANCE-ACT-RECORD.md", which is false if the owner gives the act in the
recommended option-1 form. Changing the header changes the file digest, so
this belongs to whatever regeneration follows the owner's choice of form;
suggest the packet or migration plan say that the header is re-rendered to
match the chosen form.

**Finding 3 — Brief criterion 9's "no 64-hex digest in any Markdown file of the package" is false by construction once raws are stored** (note)
`REVIEW-BRIEF.md:81-84` vs `REVIEW-BRIEF.md:112-117`; `reviews/R-RFC5-PROJECT-DOCUMENTATION-CLASS-1-RAW.md:3`.
The brief requires each raw's head to carry the manifest file's SHA-256 and
also says no 64-hex digest may appear in any Markdown file of the package. The
retained round-1 raw carries one (as this raw does), as the brief requires;
`check_governance.py` exempts `-RAW.md` and reports 0 FAIL. The criterion
should exclude retained `-RAW.md` files for any later round, or a literal
reading fails every confirmed package.

## Summary

No blocking finding; three notes. The patch is mechanically exact (independent
`patch` + `sha256sum` equals the manifest row), widens no consent, leaves the
composite rule, RFC5-15 and RFC5-16 intact, and claims no authority. Both
round-1 blocking findings are resolved: the signals sub-bullet no longer
constrains classification-policy content, and every published sweep figure
reproduces from the printed predicate at both commits, with group counts
summing to 140.
