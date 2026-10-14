# R-PWB-RELEASE-LABEL-AMENDMENT-4 — fresh-context confirmation review, round 4
Reviewed commit: 8acb0795562c548201e24eb6a20d8eddc66f04d1
Manifest SHA-256: 73cca446620b99bc6626adcc2530817fb4ef2c55d6a428d20f16150077fbca61
Verdict: REVISE

## Provenance and method

- **Commit.** I ran `git fetch origin main` and `git checkout --detach 8acb0795562c548201e24eb6a20d8eddc66f04d1`. `git rev-parse HEAD` returned that commit.
- **Manifest digest.** I computed it two ways and they agree:
  - `git show 8acb0795…:.syzygy/governance/contracts/candidates/pwb-release-label-amendment/PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt | sha256sum`;
  - `sha256sum` of the file in a fresh clone at the same commit.

  It is the digest of the file, not a row inside it.
- **Where the checks ran.** In a fresh `git clone` of the reviewed commit (rule 7), not in the review worktree. I read the output of each one, not just its exit code:
  - `build_pwb_release_label_amendment.py --check`: "release-label candidate matches 11 proposed subjects (7 patched); 17 requirements, 56 scenarios; structure, regeneration, contract coverage, sibling classification and pending-patch order verify".
  - `--selftest`: "37 structure mutants, patch drift, an unclassified sibling, the pending patch population, and divergent and failing application orders all fail closed on their own predicates".
  - `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
  - `build_polaris_project_wide_contract_coverage.py --check` on the current tree: "matches regeneration — 324 clauses represented". The builder's own `--check` also runs it over the proposed bytes.
  - Sibling builders' `--check`, all of which pass at this commit:
    - accessible-name: "17 requirements, 54 scenarios … pending-sibling composition (pairwise, and one result in every order) verify";
    - class-granular: "17 requirements, 56 scenarios … pending-patch order verify";
    - opening-index: "17 requirements, 54 scenarios … pending-sibling composition … verify".
- **Independent composition check.** My own script applied every pending package's patch with `patch -F0` to a scratch copy of each subject, in every order. The four packages are release-label, accessible-name, class-granular and opening-index.
  - `spec.md`: 4 patches, 24 orders, 1 distinct result, 0 failing orders. This confirms the builders' claim.
  - `proposal.md`: 2 patches, 1 result.
  - `design.md`: 2 patches, both orders apply, 2 distinct results.
  - `CAPABILITY-COVERAGE.md`: 2 patches, and the second fails in both orders.

  The last two results are Note 8.
- **My own mutants (rule 6).** I mutated the proposed spec bytes with my own script and ran `structure_findings`:
  - Deleting the falsifier limb "a tag presented as unmoved, unchanged or stable", or rewording "Tests 2, 4 and 5 apply to its own recorded listing", each fails on its own required-phrase predicate.
  - Three mutations fail only on the dependency-digest predicate and on no content predicate: widening the status-line exception to "any element the implementation marks as a provenance stamp"; deleting the stamp's purpose clause; and narrowing the stability terms to `unmoved` alone. See Note 7.
- **Proposed bytes.** Read through `--diff`. I re-computed the totals:
  - contract coverage 628 → 629, covered 136 → 137, believed-not-applicable 245 → 245, so 137 + 247 + 245 = 629;
  - repair delta 92/77/60/27/5 → 94/78/61/27/6;
  - capability 27/6/0/33 → 28/6/0/34.

  All agree with the printed figures.
- **Signed bytes.** The two warrant lines are the only `-` lines in `spec.md.patch`. The builder checks that every other requirement is byte-identical.
- **Anchors re-read at this commit (rule 8).** Every quotation matches its clause:
  - RFC2-2 (`snapshot-and-evaluation-core.md` line 112);
  - RFC2-24 row 10 (`rendering-vocabularies.md` line 139);
  - RFC4-11 reads (`named-adapters.md` lines 108 and 110) and "it never reconstructs commit history it cannot reach" (lines 124–125);
  - RFC6-15 (line 314);
  - VIS-2 (`vision.md` lines 133–135).
- **Reading scope.** I read what the brief's Round 4 section allows:
  - the round-3 raw;
  - `ROUND-3-DISPOSITIONS.md`;
  - the implementation files it names, plus `production-reobserve.ts` and `model.ts`, to trace the footer's evaluation identity;
  - PWB-REQ-011, PWB-REQ-014 and PWB-REQ-020 in the signed spec;
  - POC-REQ-001 and a term sweep of the POC spec.

  I did not open `ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md` or any other raw.

## Round-3 findings: are they repaired?

Each repair is judged against the round-3 raw, not against the disposition's account of it.

| R3 # | Raw's finding | Status at this commit |
|---|---|---|
| 1 (revise) | Naming-site definition counts provenance stamps and verbatim Butlers text. Either reading fails CC-SPEC-4. | **Partly repaired.** The verbatim-text conflict with PWB-REQ-014 is closed: Butlers-declared verbatim text is excepted and checked byte-identical. "Identities are not owner-visible text" is gone. But the provenance-stamp exception moves the judgment instead of removing it. A stamp is recognised only by the implementation's own mark and by its text being a bare id. Nothing decides that a stamp is per-claim provenance rather than a naming of the revision. The ledger itself prescribes wrapping prose namings in stamps. See Finding 1. |
| 2 (revise) | Oracle cannot derive either not-read form. | **Repaired.** Construction records are checker-owned. Tests 1 and 3 read them, and tests 2, 4 and 5 read the listing. The untagged decide-line names the records, and oracle independence includes them. On the shallow fixture whose captured history holds a reaching tag, a checker that follows the text now expects not read. A residual on fixture coverage is Note 5. |
| 3 (note) | Shared status line is inside the sweep; the ledger says otherwise. | **Repaired.** The line is excepted by name, the ledger is marked at the sentence, and Question 5 puts the content choice to the owner. A residual on the stated warrant and on the mark is Note 3. |
| 4 (note) | "Nothing presents a tag as unmoved" has no observable, decide-line or falsifier. | **Repaired.** It now has a scoped prohibition, a fifth sweep, a decide-line and a falsifier limb. A residual is Note 4. |
| 5 (note) | Where the tied-name expansion lives; the machine record as a "site in a label unit". | **Repaired.** The expansion is inside the label unit, and the equality line covers "each label unit, its expansion included". The label-unit predicates apply to page sites only. |
| 6 (note) | Shared-prefix selftest predicates; order-blind lost-line guard. | **Repaired.** `phrase_finding` gives each mutant the full text of its own phrase. `lost_lines` is a subsequence check, and the "signed line moved" mutant fails on its predicate. A residual is Note 7. |
| 7 (note) | Two stale Observed measurements. | **Repaired.** Re-measured and marked at the sentence, old text kept. I spot-checked each figure at this commit and all hold:<br>- `page-shell.ts` line 47;<br>- `orrery.ts` lines 197 and 212;<br>- `trajectory.ts` line 236;<br>- `git-observation.ts` lines 62, 106 and 161, all `rev-parse HEAD`, with no `refs/tags`;<br>- `reevaluation.ts` lines 5 and 23;<br>- `polaris.ts` lines 241, 299, 1200, 1244, 298, 1190, 1209 and 1870–1882. |

## Criteria

1. **Direction content: not fully met.** "The release label leads" is not enforced on any naming the implementation marks as a stamp (Finding 1). The departures are named and put to the owner as Q2–Q5 and §"Departures" 1–5.
2. **Specification bar: not met** (Finding 1). Excepting a provenance stamp depends on a mark the implementation sets, and nothing structural decides it. The falsifier has no limb for a naming disguised as a stamp.
3. **Contract claims: met.** The anchors match, and the `RFC4-11.r1` observation now rests on checker-owned construction records.
4. **Signed bytes: met.**
5. **Mechanics: met.** Every check passes in a clone, the totals equal computation, and the sibling builders pass.
6. **Honest claims: met, with Notes 2 and 3.** The ledger's inventory of Polaris visible ids misses the footer.
7. **Plain language: met.**

## Findings

**Finding 1 — the provenance-stamp exception is decided by the implementation's own mark, so "names the revision only in a label unit" and "the release label leads" can be met by marking every naming as a stamp** (revise)

The proposed text:

- "Polaris names the observed revision only in a label unit."
- The prohibition excepts "a provenance stamp, whose whole text is a revision's full object id or its first twelve hexadecimal digits, giving the revision at which a claim, source, leaf or refusal was read or to which it is bound. It is the identity that claim binds to, not a naming of the revision, and it carries no label".
- The stamp's only decide-line: "every provenance stamp's whole text a full object id or its first twelve hexadecimal digits".
- The floor: "at least one label unit on every Polaris page".

Only two things decide whether an occurrence is an excepted stamp:

1. the implementation's own mark, since the element is "marked as its kind";
2. its text being a bare id.

The stamp's purpose, "giving the revision at which a claim, source, leaf or refusal was read or to which it is bound", is in no decide-line. My mutant that deletes that clause fails no content predicate. A bare twelve-digit id is exactly what a naming of the revision looks like in the not-read and untagged forms, so the text-shape test does not tell a stamp from a naming. The delta's claim that "Each stamp's whole text must be a revision id, so a stamp cannot hide a naming" (§"Choices the cycle-2 repair made", item 2) does not hold.

[Observed] The package prescribes this route itself. `IMPACT-LEDGER.md` §"Polaris visible ids an implementation would mark" says "each prose or refusal occurrence either wraps its id in a marked stamp or becomes a label unit". The prose occurrences it names include:

- `polaris.ts` line 1190: "Declared project shape of ${repositoryId} at revision ${12 hex}.";
- line 1209: "Revision `<12 hex>` (requested …)", in the shape identity section.

These are the page's primary namings of the observed revision.

Falsifier the text does not catch. A Polaris page that:

- puts one label unit in its footer;
- renders "Declared project shape of butlers at revision `<stamp>abc…</stamp>`" and "Revision `<stamp>abc…</stamp>`" in the identity section;
- marks every other revision mention as a stamp.

That page passes every decide-line:

- one label unit per page;
- zero swept occurrences outside units and excepted elements;
- every stamp's whole text is an id;
- equality inside the unit.

Yet the release label leads nowhere a reader looks for the revision. The CC-SPEC-4 judgment the round-3 raw asked to remove ("the checker has to judge which visible hex strings are identities and which name the revision") has moved into the implementation's choice of mark, which the checker trusts. A check that trusts the system under test's own classification is not independent.

Two related gaps:

- "Lead with" has no observable of its own. No decide-line says where a label unit sits relative to the content that uses the revision, and none checks that the label precedes the full object id within the unit. The text says the id is "beneath", and only its presence is decided ("the full object id in each label unit").
- The falsifier list has no limb for "a naming of the observed revision presented as a provenance stamp".

Proposed repair: make the stamp structural and checkable without the implementation's say-so. For example:

- a provenance stamp is only the revision element of a citation attached to an anchored claim, source, leaf or refusal (the existing `cite@code` citation shape), and the checker verifies that attachment from the anchor records;
- a revision id inside a prose sentence, a heading or the shape-identity section is never a stamp;
- the shape-identity statement, or the first naming of the revision in document order on each page, is a label unit, with the label decided to precede the full id within it;
- add the falsifier limb "a naming of the observed revision marked as a provenance stamp".

If the owner prefers bare stamps in prose, say so as a named choice. The text should then stop claiming that a stamp "cannot hide a naming".

**Note 2 — the footer's evaluation identity shows the full observed revision and is missing from the inventory** (note)

[Observed] Polaris's page footer renders `Evaluation <code>${model.evaluation.snapshot}</code>` (`polaris.ts` line 1881, inside the `pageShell` call at 1870–1882). The production snapshot begins `${repositoryId}:${capture.repositoryRevision}` (`production-reobserve.ts` lines 85–89). The recorded evidence carries snapshots of that shape, `butlers:<40 hex>|working-tree:…`, for example the `docs/evidence/pwb-p4-5-fresh-checkout-demo-*.json` records.

So every Polaris page shows the full object id in footer text that matches none of the three exceptions:

- it is not a label unit;
- its whole text is not a bare id, so it is not a stamp;
- it is not Butlers text;
- it is not the status line.

The signed Observable requires Polaris to expose "every deterministic input and per-emission identity", and RFC6-15 makes answers evaluation-stamped. So the amended text forces either a reformat of the evaluation identity or a stamp wrapped round its revision part. The second route works only through Finding 1's gap. The ledger's re-measured list of "Polaris visible ids an implementation would mark" at `814fbcc1` omits this occurrence. Name it, and say which treatment the text intends.

**Note 3 — the status-line exception's warrant and mark** (note)

- **The warrant.** The exception says the status line is one "which the POC specification governs". I swept `openspec/**` for `operability`, `status line` and `humanStatus`. There are 0 hits in `openspec/changes/three-surface-poc-experience/`; the only hits are `openspec/README.md` line 53 (unrelated) and two PWB coverage rows that use "operability" in another sense. [Inferred] No POC requirement names the status line. POC-REQ-001 governs observation provenance, not this line. So excepting the line leaves its revision display on Polaris governed by neither specification. Question 5 discloses the choice, but the sentence "which the POC specification governs" is unanchored (rule 8).
- **The mark.** Each excepted kind must be "marked as its kind". The delta says the package "changes nothing in `page-shell.ts`". [Inferred] The existing `data-human-status` attribute could serve as the mark, but the text does not say so. Otherwise the mark itself is a change to the POC-governed component. Say which.

**Note 4 — the stability sweep is narrower than its falsifier and is blind to split text nodes** (note)

The falsifier limb is "a tag presented as unmoved, unchanged or stable". The decide-line is "zero stability terms found by the fifth sweep", over a closed list of five terms in "every other owner-visible text node … that holds a captured tag name".

- Choice 4 discloses that a paraphrase outside the list is not caught. A paraphrase also falsifies the requirement under the broader limb, so an implementation can falsify the requirement and still pass the oracle.
- Separately, the sweep is per text node. `<code>v1.0.23</code> unchanged` puts the tag name and the term in different nodes, so the sweep misses it even for a listed term.

Either align the limb to the list or name the gap there, and define the sweep over an element's whole text rather than its text node.

**Note 5 — construction records name conditions that no fixture builds** (note)

The construction records cover:

- the tag-set and ancestry read admission;
- a ref made to fail;
- a commit made unreadable;
- a shallow or graft boundary.

Test 3 holds on any of "the ancestry read is not admitted, a commit was made unreadable or a shallow or graft boundary was imposed". The fixture list builds only shallow clones for test 3. It has no fixture with:

- an unadmitted ancestry read while the tag set is admitted;
- an unreadable commit in a complete-depth clone;
- a grafted object database.

Two of test 3's three conditions are therefore unobserved. Add those fixtures, or narrow test 3's observed population and say so.

**Note 6 — "every Polaris page" has no stated population** (note)

The floor "Every Polaris page SHALL present at least one label unit" and the denominator "every label unit on every Polaris page" need a closed page population, and the text does not give one. Candidate members a checker must decide on include:

- the exact-source route's pages (PWB-REQ-011);
- refusal responses (`verbatim-route.ts` line 82);
- the generation draft view `GET /polaris/draft/<runId>`, which PWB-REQ-020 says "carries no project-shape identity", so a label unit there would conflict.

Name the population, for example the human HTML routes under `/polaris`, excluding the PWB-REQ-020 machine and draft views.

**Note 7 — two residual weaknesses in the builder's guards** (note)

- **Wording the phrase guards miss.** Three of my mutants fail only on "proposed GOVERNING-DEPENDENCIES does not name the proposed spec digest" and on no content predicate:
  - widening the status-line exception;
  - deleting the stamp purpose clause;
  - narrowing the stability term list.

  At these bytes the digest guard catches any edit. After a later `--write` regeneration, though, these three load-bearing wordings would have no content guard. Add them to `REQUIRED_ONCE`.
- **Duplicate lines.** `lost_lines` matches greedily with `lines.index(line, position)`. A signed line that has an identical twin later in the new text (a blank line, a repeated scenario bullet) can be matched to the twin, so moving or deleting such a line goes unreported. [Observed] The current diff moves no signed line.

**Note 8 — the order check covers `spec.md` only; `design.md` and `CAPABILITY-COVERAGE.md` collide with class-granular** (note)

My independent composition run, described above, found two collisions:

- release-label's and class-granular's `design.md.patch` both apply in either order, but give two different results, each with two decisions numbered `### 12.` ("Name the revision by its release label" and "Read each class of a source on its own");
- their `CAPABILITY-COVERAGE.md.patch` files fail in both orders, since both add row 34.

The delta's §"Pending siblings" discloses this and routes it to P-86's Question 5 ("whichever … is signed second is regenerated … and reviewed again"). It is recorded here because the builder's "pending-patch order verify" covers the spec only. A `design.md` applied second without regeneration would silently carry a duplicate decision number.

Counts: 1 revise-level finding (1), 7 notes (2–8), 0 blocking.
