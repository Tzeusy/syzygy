# R-PWB-RELEASE-LABEL-AMENDMENT-2 — fresh-context review, round 2, PWB release-label amendment
Reviewed commit: f0ad565e488432e42019c27d1e348419e5d4a892
Manifest SHA-256: 3ee1e2fdfb21c976b2a8ac1bd352f126ee7af43f22a993d503ef2b00787c646d
Verdict: REVISE

Reviewer: fresh-context agent, 2026-10-03. Read only the brief's artifact and
governing references; did not read `ROUND-1-DISPOSITIONS.md` or anything under
`docs/reviews/`. Proposed bytes were read by applying the seven patches in a
scratch clone (`review-zeaf-apply`), never in the reviewed clone; the reviewed
clone's `git status --short` was empty after every check. Line numbers for
"proposed spec.md" are lines of the applied
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`.

## Mechanical record

- [Observed] Manifest digest computed by `git show f0ad565e…:<manifest> | sha256sum`
  and by `sha256sum` on the worktree file: both
  `3ee1e2fdfb21c976b2a8ac1bd352f126ee7af43f22a993d503ef2b00787c646d`.
- [Observed] `python3 scripts/build_pwb_release_label_amendment.py --check`
  (PYTHONDONTWRITEBYTECODE=1), output: "release-label candidate matches 11
  proposed subjects (7 patched); 17 requirements, 55 scenarios; structure,
  regeneration, contract coverage and sibling classification verify", exit 0.
- [Observed] `--selftest`, output: "selftest: 19 structure mutants, patch
  drift and an unclassified sibling all fail closed on their own predicates",
  exit 0. Each mutant is checked against its own expected finding prefix
  (`scripts/build_pwb_release_label_amendment.py:605-613`).
- [Observed] Independent rule-6 mutants in a third scratch clone, not in the
  selftest: one manifest row digest changed → "manifest differs from
  deterministic proposed-byte regeneration"; `CONTRACT-COVERAGE.md.patch`
  covered count 137→138 → "contract-coverage --check fails … DRIFT"; RFC4-11.r1
  disposition covered→unknown-uncovered in the repair patch → "repair row
  missing: RFC4-11.r1" and "declared repair totals mismatch: (94, 78, 61, 27,
  6) != (94, 78, 60, 28, 6)". All three fail closed.
- [Observed] `python3 scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL
  (52 checks)"; no WARN line names this package or its builder.
- [Observed] All 7 patches apply with `git apply`; `sha256sum -c` of the 11
  manifest rows over the applied tree: 11 OK.
- [Observed] Over the applied tree:
  `build_polaris_project_wide_contract_coverage.py --check` → "Polaris
  consequence matrix matches regeneration — 324 clauses represented";
  `build_polaris_project_wide_spec_dependencies.py --check` → "Polaris
  dependencies match regeneration — 17 requirement(s)". (An earlier `--help`
  invocation of the dependency builder in the scratch copy wrote
  `GOVERNING-DEPENDENCIES.md`; its sha256 afterwards equalled the manifest row
  `999d9db3…`, i.e. regeneration equals the proposed bytes.)
- [Observed] Capability totals recomputed by script over the applied table: 34
  rows, 28 `covered`, 6 `lawfully out of scope`, 0 other; printed "Totals: 28
  covered, 6 lawfully out of scope, 0 Unknown/unresolved; 34 total." and
  "Population: 34".
- [Observed] Repair delta recomputed by script: before 92 rows / 77 distinct
  superseded / 60 covered / 27 unknown / 5 N/A; after 94 / 78 / 61 / 27 / 6,
  equal to the declared totals. Effective population 628→629 and covered
  136→137 in `CONTRACT-COVERAGE.md` follow (−c4 N/A, +r1 covered, +r2 N/A).
- [Observed] `git diff pwb-tree-framing-amendment-v1.0 HEAD --
  openspec/changes/polaris-project-wide-butlers-model/` is empty: the current
  subject bytes are the bytes the tree-framing v1.0 sign-off tag carries.
- [Observed] Applied `check_spec_reconciliation.py --check`: R2 FAIL (12) and
  R3 FAIL (3); un-applied clone: R2 OK. These are the residuals the delta
  names (`SEMANTIC-DELTA.md:280-290`). R6's two stale pins already fire on the
  un-applied tree (pin `0d50f8f4…` vs current `d0ac6ba2…`), so they are not
  introduced by this package.
- [Observed] `IMPACT-LEDGER.md:10-14` predicate re-run by script at `0a10977b`:
  1,947 paths, 74 files — matches. At HEAD it reads 1,963 / 86; the ledger is
  dated to `0a10977b`, so this is not a defect.

## Findings

**Finding 1 — The not-read form mandates a false statement under test 3** (revise)

Carried note 1, confirmed. [Observed] Proposed spec.md:323 makes test 3 "Not
read, when the captured ancestry is incomplete" — a case reached only after
test 1 failed, i.e. the tag set *was* captured (spec.md:319-320). Yet
spec.md:331-333 requires, for every not-read form, "the statement that release
tags were not read", and the scenario repeats it for the incomplete-ancestry
case (spec.md:446-451: "or R's captured ancestry is incomplete and no captured
tag peels to R … states that release tags were not read"). In that case the
statement is false: the tags were read and the history was not.
`SEMANTIC-DELTA.md:87-88` carries the same wording, while
`OWNER-DECISION-PACKET.md:21-22` says the opposite ("used whenever the tags, or
the history needed to judge them, were not read"), so the owner is shown one
rule and would sign another. [Inferred] Criterion 1 ("an untagged commit shows
a short id, honestly labelled") is not met: an untagged commit observed
through a shallow clone would be rendered with a false reason sentence, and
the oracle cannot catch it because no decide-line checks the statement's
text (spec.md:398-406 check only "zero labels stating untagged"). Repair:
"release tags, or the history needed to judge them, were not read" (or a
distinct statement per not-read test) in spec.md, the scenario, the delta and
the design flowchart node text if changed; add a decide-line for the
statement.

**Finding 2 — `RFC4-11.r1` claims coverage the fixture set cannot exercise** (revise)

[Observed] The repair row claims `covered:PWB-REQ-001` for "A count over commit
history is computed only from completely captured ancestry and is never
reconstructed from history the adapter cannot reach"
(`CONTRACT-COVERAGE-REPAIR-DELTA.md` applied; `SEMANTIC-DELTA.md:167-172`
says "the incomplete-ancestry not-read test and the shallow-clone fixture
observe it"). The fixture list is closed ("The fixtures are:", spec.md:360-371)
and its only incomplete-ancestry fixture is "a shallow clone whose missing
history holds the only reaching tag" (spec.md:368). In that fixture no tag is
visible, so no implementation can produce a count; it tests only the
never-say-untagged limb. [Inferred] An implementation that computes
`git describe`-style counts from a shallow history whenever a reaching tag is
visible in the captured part — the exact behaviour r1 forbids — passes every
listed fixture. Criterion 3 ("no contract-coverage row claims something the
oracle does not observe") is not met for the count limb. Repair: add a fixture
"a shallow clone whose captured history holds a reaching tag" (expected form
not read), or narrow r1 to what the existing fixture observes.

**Finding 3 — The naming-site denominator counts sites the requirement makes label-free** (revise)

[Observed] The obligation's scope is "Wherever Polaris names the observed
revision" (spec.md:290), but the oracle's denominator is "every element of
every Polaris page and of the machine answer that carries the revision's full
object id, its first twelve hexadecimal digits, or a label" (spec.md:382-385),
decided by "zero sites without a label" (spec.md:399). The same requirement
says "every claim, evaluation identity, link and comparison binds to" the
object id (spec.md:294-296), and the signed text already sends every
project-shape fact to machine readers with its source identity and the
revision identity (spec.md:284-288). [Inferred] Elements that lawfully carry
the full object id without a label — a link target or identity that binds to
it, a per-fact revision stamp in the machine answer, and the full-id element
beneath the label itself if it is a separate element — fall in the
denominator, so a conforming implementation fails the oracle, or the checker
must judge which elements "name" the revision. CC-SPEC-4 requires an
effective oracle that decides "without judgment"
(`SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:191-193`); criterion 2 is not
met for this sweep. Repair: define naming sites as the human-visible text
presenting the revision (and the machine answer's label record), and leave
identities and link targets to the separate tag-name sweep (spec.md:391-392).

**Finding 4 — "Release tag" is undefined while the rule counts every tag** (note)

Carried note 2. [Observed] Test 5 and its scenario say "no release tag
reaches" (spec.md:328-329, 442), while the tag set is "every ref under
`refs/tags/`" (spec.md:304-305) and Question 4 recommends exactly that
(`OWNER-DECISION-PACKET.md:92`). [Inferred] Under the every-tag rule the
untagged statement is still true (no tag of any kind reaches), and under a
declared pattern it would also be true, so nothing renders false and the
oracle is unaffected; and Question 4 is put to the owner rather than settled
silently, so CC-SPEC-6 is satisfied. The term is still undefined in the
requirement text: say "no tag reaches" or define "release tag" as a captured
tag, so the wording does not pre-empt or contradict the Question 4 ruling.

**Finding 5 — Signed PWB-REQ-001 sentences are extended, and the builder does not guard them** (note)

[Observed] Over PWB-REQ-001, a line diff of signed vs applied shows four
replaced line groups, each an extension of a signed sentence: "per-emission
identity." → "…, and every label's form, values and full object id."; the
oracle-independence and falsifier sentences gain a following sentence; the
warrants gain VIS-2, RFC2-2, RFC2-24. Every other requirement block and the
pre-requirement head are byte-identical (script over both trees: head same,
17 ids same, changed = [PWB-REQ-001]). Criterion 4 is met: every signed word
survives, as a prefix. But `KEPT_IN_001`
(`scripts/build_pwb_release_label_amendment.py:140-144`) pins only the opening
WHEN-sentence and the signed scenario title; the lost-line guard used for the
companions is not applied inside PWB-REQ-001, so a later version could delete
a signed Observable/Oracle/Falsifier clause and `--check` would pass.

**Finding 6 — Moved-tag disclosure on tied, unnamed tags is unstated** (note)

[Observed] A moved tag is disclosed "wherever a label names that tag"
(spec.md:342-344), while tied names are "carried in the machine answer and
expandable on the surface" (spec.md:334-336). [Inferred] Whether a moved tag
that is tied but not the first in codepoint order must be disclosed (in the
machine answer, or in the expansion) is not decided by the text, and no
fixture combines a tie with a move. A related edge: a tag ref whose peel fails
while the rest of `refs/tags/` reads is not plainly "reading it failed"
(spec.md:319-320). Neither blocks the four-form rule on the listed fixtures.

## Criteria summary

1. **Direction content** — not met. The four direction elements are carried
   (spec.md:290-346), and every departure is named and put to the owner (read
   change: delta §"The read…" and Question 2; Trajectory/Orrery: Question 3;
   moved-tag limits: departure 3; tag population: Question 4; plus the
   PWB-REQ-007/020 departure). But the not-read statement is false under test
   3 and contradicts the packet (Finding 1).
2. **The specification bar** — not met. One form (state projection/query,
   spec.md:280), scope, fixtures, observable, independence and falsifier are
   present, and the five ordered tests decide every revision on the stated
   inputs without judgment; the naming-site denominator does not (Finding 3).
3. **Contract claims** — not met. The quotes of RFC2-2 (snapshot-and-
   evaluation-core.md:112-114), RFC2-24 row 10 (rendering-vocabularies.md:139),
   RFC4-11 reads and "never reconstructs commit history it cannot reach"
   (named-adapters.md:105-125), RFC6-15 (RFC-0006:312-316) and VIS-2
   (vision.md:133-135) are verbatim, RFC1-10 is correctly held to analogy,
   and the only moved base row is `RFC4-11.c4`; but r1's covered claim is
   wider than the fixtures observe (Finding 2).
4. **Signed bytes** — met (Finding 5 is a note).
5. **Mechanics** — met: `--check` and `--selftest` pass, mutants fail on their
   own predicates, dependency file equals regeneration, coverage `--check`
   passes over proposed bytes, capability and repair totals equal computation.
6. **Honest claims** — met: no adoption claimed, no read authorized
   (delta §"What this does not do"; packet "What signing does not do"), no
   implementation scheduled, and the four residuals are named and verified
   against `check_spec_reconciliation.py` (census 17/51, PWB-REQ-001 at 1;
   successors tuple with tree-framing only).
7. **Plain language** — met, subject to Finding 1: a fresh reader can restate
   what changes (PWB-REQ-001 and its companions) and what does not (other
   requirements, registry, Trajectory/Orrery, implementation).
