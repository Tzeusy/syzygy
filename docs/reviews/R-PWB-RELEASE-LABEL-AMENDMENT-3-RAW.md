# R-PWB-RELEASE-LABEL-AMENDMENT-3 — fresh-context confirmation review, round 3
Reviewed commit: 7baea99151f68ac883f27d1ed4c79e608dce08bd
Manifest SHA-256: 610880fd9ce477bf094856dee7c4af90f5231d4186b4e413bdf242fc015c1dd1
Verdict: REVISE

## Provenance and method

- Commit: fetched `candidate/p85-round2-repairs`, detached at
  `7baea99151f68ac883f27d1ed4c79e608dce08bd`, `git rev-parse HEAD` confirmed.
- Manifest digest: `git show 7baea991…:.syzygy/governance/contracts/candidates/pwb-release-label-amendment/PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt | sha256sum`,
  then confirmed by a second method (`sha256sum` of the file in a fresh clone
  at the same commit). The two agree. It is the digest of the file, not a row
  inside it.
- Checks were run in a fresh `git clone` checked out at the reviewed commit
  (rule 7), not in the review worktree:
  - `build_pwb_release_label_amendment.py --check`: "release-label candidate
    matches 11 proposed subjects (7 patched); 17 requirements, 55 scenarios;
    structure, regeneration, contract coverage, sibling classification and
    pending-patch order verify".
  - `--selftest`: "30 structure mutants, patch drift, an unclassified sibling,
    the pending patch population, and divergent and failing application
    orders all fail closed on their own predicates".
  - `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
  - `build_polaris_project_wide_contract_coverage.py --check` (current tree):
    passes, 324 clauses. The builder's `--check` runs the same generator's
    `--check` over the proposed bytes in a scratch mirror (`run_coverage`,
    `coverage_findings`), and that passed above.
  - Sibling builders' `--check` (class-granular, anchor-resolution,
    opening-index, accessible-name): all four pass at this commit, which
    supports the delta's §"Pending siblings" claim.
- Proposed bytes were read through `--diff`. Totals were re-computed by hand
  against the diff: contract coverage 628 → 629 (−1 base row `RFC4-11.c4`,
  +2 repair rows), covered 136 → 137, believed-not-applicable 245 → 245;
  repair delta 92/77/60/27/5 → 94/78/61/27/6; capability 27/6/0/33 →
  28/6/0/34. All agree with the printed figures.
- Anchors re-read at this commit (rule 8): RFC2-2 (snapshot-and-evaluation-core.md
  line 112), the RFC2-24 row for `source-uncaptured-or-unreachable`
  (rendering-vocabularies.md line 139), RFC4-11 reads (named-adapters.md lines
  108–111) and the fidelity limb "it never reconstructs commit history it
  cannot reach" (lines 122–125, wrapped), RFC6-15 (line 314), VIS-2
  (vision.md lines 133–135), and the matrix row `RFC4-11.c4`
  (RFC-0004-0006.md line 65). Every quotation in `SEMANTIC-DELTA.md` matches
  its clause.
- **Disclosure about reading scope.** The round-3 section of the brief says
  not to read `ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md` or anything
  under `docs/reviews/`. The dispatcher told me to check each round-2 finding
  against the "Repairs, 2026-10-14" section of `ROUND-2-DISPOSITIONS.md`, so
  I read that file, and only that file. I did not open `ROUND-1-DISPOSITIONS.md`
  or any raw under `docs/reviews/`. The findings below are judged on the
  current bytes against the brief's references. Where I say whether a round-2
  finding is repaired, I am going by the finding as that record summarizes it.

## Round-2 findings: are they repaired?

| R2 # | Subject (as summarized in the record) | Status at this commit |
|---|---|---|
| 1 | Not-read statement false under test 3 | **Repaired.** Each not-read test has its own exact statement. The scenario, design node, delta and packet agree. A decide-line and a falsifier limb check the statement. |
| 2 | `RFC4-11.r1` claims more than the fixtures observe | **Partly repaired.** The fixture and the falsifier limb were added. But the oracle procedure as written cannot compute that fixture's expected form, so the coverage still rests on an undecidable step. See Finding 2. |
| 3 | Naming-site denominator counts label-free sites | **Partly repaired.** Attribute values, link targets and identities are now excluded. Owner-visible per-fact revision stamps, the class the finding named, are still counted, and verbatim Butlers text is newly counted. See Finding 1. |
| 4 | "Release tag" undefined | **Repaired.** The term is defined by the captured tag set and follows Question 4. |
| 5 | Signed PWB-REQ-001 lines unguarded | **Repaired.** The diff shows only `+` lines inside PWB-REQ-001 apart from the two warrant lines. The lost-line guard covers the whole block, and the four new mutants pass in the selftest. A residual is in Finding 6. |
| 6 | Moved tags on tied names; single failed peel | **Repaired in text and fixtures.** A residual about where the expansion lives is in Finding 5. |

## Criteria

1. Direction content: met. Departures are named and put to the owner as
   Q2–Q4, plus §"Departures" items 1–5.
2. Specification bar: **not met** (Findings 1 and 2).
3. Contract claims: anchors met. **Not met** for `RFC4-11.r1`'s observation
   (Finding 2).
4. Signed bytes: met. The builder checks byte identity of every other
   requirement, and the diff confirms it.
5. Mechanics: met. All four checks pass in a clone, the totals equal
   computation, and the dependency patch equals regeneration.
6. Honest claims: met, with Notes 3 and 7.
7. Plain language: met. The delta and packet restate the change clearly.

## Findings

**Finding 1 — the naming-site definition still counts the per-fact revision stamps round 2 named, and now counts verbatim Butlers text too** (revise)

The proposed text: "Polaris names the revision wherever its owner-visible
text shows the revision's full object id, its first twelve hexadecimal
digits, or the project's name followed by a captured tag's name. Attribute
values, link targets and identities are not owner-visible text." The oracle
enumerates "in the owner-visible text of every Polaris page, every occurrence
of the revision's first twelve hexadecimal digits … every occurrence of the
project's name followed by a captured tag's name", and "zero sites outside a
label unit" decides.

[Observed] Polaris today renders the observed revision's twelve-digit prefix
in visible text at many places that are per-claim provenance, not a naming of
the revision:

- `apps/three-surface-poc/src/polaris.ts` lines 241, 299, 1200 and 1244:
  `source@<code data-parity-field="provenance-revision">…slice(0, 12)</code>`
  citations, one per anchored claim;
- line 1209: the shape fact line "Revision `<12 hex>` (requested …)";
- `verbatim-route.ts` line 82 and `capability-detail.ts` lines 231 and 238:
  refusal sentences;
- the shared status line, `page-shell.ts` `humanStatusLine` (line 47), which
  Polaris renders through `pageShell({ …, status })` (`polaris.ts` lines
  1870–1882; `page-shell.ts` line 127).

Under the amended text there are only two readings, and both fail the bar:

- **Literal reading.** Every one of these is a naming site, so each
  provenance citation must become a full label unit: the label, the
  statement, the 40-digit object id beneath, and any moved-tag disclosure.
  That repeats the label unit once per anchored claim. The delta names no
  such consequence, and [Inferred] it conflicts with the response-ceiling
  budget recorded for `/polaris`.
- **Narrow reading.** A provenance stamp is an "identity" and so excluded.
  Then the checker has to judge which visible hex strings are identities and
  which name the revision. That is the CC-SPEC-4 judgment the round-2
  finding asked to remove. "Identities are not owner-visible text" does not
  say what makes a visible string an identity.

The project-name limb adds a new conflict. PWB-REQ-014 requires that
"Butlers-declared text SHALL stay verbatim in its own leaf", and the scenario
"An opening above Butlers text stays outside it" requires the verbatim text
to be "byte-identical". Suppose a Butlers source's verbatim text contains
"Butlers" followed by a captured tag name, such as a release note. Then that
text is a naming site that must lie in a label unit, and wrapping it breaks
the verbatim obligation. [Unknown] Whether Butlers' sources contain such text
was not read. It is a reachable case, though, and the two requirements give
no precedence between them.

Proposed repair: define a naming site positively. For example, a page
element the implementation marks as presenting the observed revision, plus
the machine label record. Then state the sweep over unmarked text as a
separate prohibition with explicit exclusions: per-claim provenance stamps
and Butlers-declared verbatim leaves. Alternatively, keep the text sweep but
exclude provenance-stamp elements and verbatim leaves by name, and say
whether provenance stamps must carry the label.

**Finding 2 — the oracle procedure cannot derive either not-read expected form, including the fixture added for `RFC4-11.r1`** (revise)

The proposed oracle: "For each fixture, the checker computes the expected
form, statement and values by applying the rule above to its own recorded
listing of the fixture's tags and peeled objects, and to its own count of
commits between each tag and the revision." Oracle independence adds:
"Expected labels come from the checker's own Git listing of each fixture,
never from the observer's captured inputs."

Tests 1 and 3 depend on conditions the stated procedure never takes as
input:

- test 1: the tag set "was not captured, because its input is not admitted
  or reading it failed";
- test 3: "the captured ancestry is incomplete".

These are facts about the observer's capture: admission, read failure, and a
shallow or grafted object database. The checker's own tag listing and its
own commit count carry neither. Independence forbids taking them from the
observer's captured inputs. So for the fixtures "a tag set whose read fails
or is not admitted", "a shallow clone whose missing history holds the only
reaching tag" and "a shallow clone whose captured history holds a reaching
tag", the procedure as written computes tagged, described or untagged from
the checker's complete listing. It never computes not read.

The effect lands on the round-2 repair itself. On the new fixture, a
checker that follows the text would expect *described*. A conforming
implementation, which shows not read, would then fail. A defective one that
counts over the partial history, the exact defect `RFC4-11.r1`'s falsifier
names, would pass. The decide-line "zero labels stating untagged in either
not-read case" also needs the not-read cases to be identified, and the text
does not say from what. So the delta's claim that two fixtures *observe* r1
(criterion 3) rests on a step the requirement leaves to the checker's
judgment (CC-SPEC-4: an oracle "by a stated procedure … without judgment").

Proposed repair: make each fixture's construction conditions checker-owned,
recorded inputs: whether the tag-set read is admitted, which ref fails to
read or peel, and the shallow or graft boundary. State that the expected
form applies tests 1 and 3 to those records, and tests 2, 4 and 5 to the
checker's listing and count. These are fixture facts, not observer inputs,
so independence holds.

**Finding 3 — the shared status line puts a POC-governed component inside this package's sweep, and the ledger says otherwise** (note)

`IMPACT-LEDGER.md` lists `page-shell.ts` under "Not covered by this
package", noting that it is "POC-governed on Trajectory and Orrery". On
Polaris pages, though, the same `humanStatusLine` shows the project
revision's twelve-digit prefix in visible text (Finding 1). So under the
amended PWB-REQ-001 it is a Polaris naming site. A single shared component
would then owe a label unit on Polaris and a short id on Trajectory and
Orrery, which interacts with Question 3. The ledger and the delta's §"Scope:
Polaris only" should say this.

**Finding 4 — "Nothing presents a tag as unmoved" has no observable, decide-line or falsifier limb** (note)

The moved-tag bullet has two parts: "Nothing presents a tag as unmoved.
Where an evaluation names no compared evaluation, no stability is stated."
This is a prohibition. Sweep 4 compares disclosures that exist, and no sweep
looks for a stability statement. No decide-line or falsifier limb covers it
either. Today's fixtures would pass an implementation that prints "tag
unchanged since the last evaluation". A falsifier limb ("a tag presented as
unmoved or stable") and a matching text sweep would close it.

**Finding 5 — where the tied-name expansion lives, and the machine record as a "site in a label unit"** (note)

- The label unit holds "the label, the statement …, the full object id
  beneath them and any moved-tag disclosure". The tied names are
  "expandable on the surface". The text does not say whether that expansion
  lies inside the label unit.
- Sweep 4 compares disclosures "in their expansion", but the decide-lines
  check equality only "in each label unit and in the label record". If the
  expansion sits outside the unit, nothing decides on it.
- Separately, the denominator includes "the machine answer's label record",
  and "zero sites outside a label unit" then applies to a machine record,
  where "label unit" (a page element) has no meaning. Say that the
  label-unit predicate applies to page sites only, and that the record is
  decided by the equality line.

**Finding 6 — selftest predicates are shared prefixes, and the lost-line guard is order-blind** (note)

- Eleven of the 30 mutants expect the same prefix, "PWB-REQ-001 carries 0 copies of
  required phrase", and the check is `any(finding.startswith(expected))`. A
  mutant is therefore satisfied by any missing required phrase, not
  necessarily its own. Each mutation is targeted, so this holds in practice.
  Even so, rule 6's "fails on its own predicate" would be met exactly by
  matching the phrase text as well.
- `lost_lines` compares lines as a multiset, so moving a signed line within
  PWB-REQ-001 (for example, a Falsifier line moved under Oracle) passes, and
  no mutant covers that.
- [Observed] The current diff moves no signed line, so criterion 4 holds for
  these bytes.

**Finding 7 — two Observed measurements in the delta are stale at the repair base** (note)

- Departure 3 rests on a grep at `0a10977b` ("No retained evaluation
  exists"). At this commit, `packages/three-surface-poc-core/src/reevaluation.ts`
  (last changed `c069f5f5`, 2026-10-03) records "the identity it supersedes"
  and says "the prior one stays nameable beside it". It is the natural
  carrier for a compared evaluation. The conclusion still holds today, since
  no tag set is captured. The stated reason should be re-measured at
  `8f1fbec7`, as the ledger was.
- §"Scope: Polaris only" cites `page-shell.ts` line 41 and `orrery.ts` line
  187 with no commit. At this commit the revision prefix is at `page-shell.ts`
  line 47 and `orrery.ts` lines 197 and 212. The residuals section's "at
  `0a10977b`" qualifier does not reach that section.

Counts: 2 revise-level findings (1, 2), 5 notes (3–7), 0 blocking.
