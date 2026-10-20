# R-PWB-RELEASE-LABEL-AMENDMENT-8 — fresh-context confirmation review, round 8
Reviewed commit: 00bbd035f4ef14a015321403dbbbe93444ccfb4b
Manifest SHA-256: 9c3b6601f0072500411cbf2bbcd8db86792dd9f86cfbf66b0a40e491f1d999d9
Verdict: REVISE

## Provenance and method

- **Commit.** I ran a fresh `git clone git@github.com:Tzeusy/syzygy.git` to `/home/tze/.cache/claude-tmp-a3f4/r8-clone`, then `git checkout --detach 00bbd035f4ef14a015321403dbbbe93444ccfb4b`. `git rev-parse HEAD` returns `00bbd035f4ef14a015321403dbbbe93444ccfb4b`, and `git status --short` is empty. Every check below ran in that clone (rule 7).
- **Manifest digest.** I ran `sha256sum` over the manifest file `.syzygy/governance/contracts/candidates/pwb-release-label-amendment/PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt` in the clean clone. It is the file's digest, not a row inside it.
- **Checks.** I read each output, not its exit code (rule 4):
  - `build_pwb_release_label_amendment.py --check`: "release-label candidate matches 11 proposed subjects (7 patched); 17 requirements, 68 scenarios; structure, regeneration, contract coverage, sibling classification and pending-patch order verify".
  - `--selftest`: "81 structure mutants, patch drift, an unclassified sibling, the pending patch population, divergent and failing application orders, a colliding companion patch, and the lost-line guard against an independent subsequence count all fail closed on their own predicates".
  - `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted". The only lines naming this package's family are two CG-1f frozen-lane entries for the round-7 raw's scratch paths, which is expected.
  - `--diff`: read in full.
- **Census, independently.** [Observed] The signed `spec.md` has 63 `#### Scenario:` headings (`grep -c`). `proposed/spec.md.patch` adds 5, so 63 + 5 = 68. The patch's only `-` lines are the two warrant lists (patch lines 357–358). The coverage totals in the diff re-add:
  - capability: 29 + 6 + 0 = 35;
  - repair delta: 61 + 27 + 6 = 94;
  - coverage: 137 + 247 + 245 = 629.
- **My own falsifier oracle (rule 6).** `/home/tze/.cache/claude-tmp-a3f4/r8_oracle.py` is a scratch script. It implements four decide-lines literally: at least one label unit; the first swept occurrence outside the status line inside a label unit; zero swept occurrences outside a label unit and the excepted elements; and every excepted identity equal to a served identity and not an id alone. It sweeps for R's first twelve hex digits. Five fragments:
  - **A**, the round-7 raw's fragment (a served source identity inside a sentence, after a label unit): **PASS**;
  - **B**, the status line as `humanStatusLine` renders it (`project <12 hex>…`), before the label unit: **PASS** (Finding 1);
  - **C**, control, a bare twelve-digit id in a sentence: **FAIL** (D3);
  - **D**, a served identity in a sentence *before* the first label unit: **FAIL** (D2) (Note 2);
  - **E**, control, an unserved identity in a sentence: **FAIL** (D6).
- **My own structure mutants (rule 6).** `/home/tze/.cache/claude-tmp-a3f4/r8_mutants.py` runs `structure_findings` over `proposed_bytes()`. The baseline is `[]`. Each mutant is killed by a phrase finding of its own, besides the expected `GOVERNING-DEPENDENCIES` digest finding:
  - scenario-5 title reverted to the cycle-5 title;
  - the limit's ", an identity by the revision's full object id" dropped;
  - the limit's "passes" flipped to "fails";
  - the design's "or an excepted identity" dropped;
  - the THEN narrowed back to "outside a citation".
- **Reading scope.** I read these:
  - `REVIEW-BRIEF.md`, in full;
  - `docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-7-RAW.md` and `ROUND-7-DISPOSITIONS.md`, in full;
  - `OWNER-DECISION-PACKET.md` and `SEMANTIC-DELTA.md`, in full;
  - the manifest;
  - `IMPACT-LEDGER.md`: line 43, lines 85–124 and a term grep, not in full;
  - the builder: its phrase tables and mutants, by grep, and lines 630–643;
  - `apps/three-surface-poc/src/page-shell.ts`, by grep (lines 29–57, 127);
  - `polaris.ts` and `polaris-source.ts`, by a `pageShell(`/`status` grep;
  - `packages/three-surface-poc-core/src/project-shape-observation.ts`, lines 325–339 and two greps.

  Every file is within the brief's lists (§"Round 8", and §"Round 6"'s implementation list). A directory listing showed the names of `ROUND-1-…` to `ROUND-6-DISPOSITIONS.md`, but I did not open them. I opened no other raw and no Butlers content, and I did not run the daemon.

## Round-7 findings: are they repaired?

| R7 # | Raw's finding | Status at this commit |
|---|---|---|
| F1 (revise) | Withdrawal incomplete: the packet summary says "an id in a sentence or heading never does", and delta cycle-3 choice 1 says "is never a stamp" | **Repaired.** [Observed] Packet lines 162–177 now say "A bare id in a sentence or heading, outside any citation, fails (Question 6)", and then "Where a citation or an identity sits is not decided: either one placed inside a sentence or heading passes, so a sentence can still name the revision through it, an identity by the full id". The old words are kept in a dated note. Delta lines 701–706 carry a dated mark at the stale sentence, with the old words quoted. A sweep over the packet, delta, ledger and diff for `never a stamp\|never does\|never counts\|leads wherever\|cannot be cast\|cannot hide` finds only marked or quoted historical text. |
| F2 (revise) | An excepted identity in a sentence passes, and neither limit covers it | **Repaired for the identity route.** [Observed] The limit reads "Where a citation or an excepted identity (below) sits is not decided by this requirement: a citation or an identity placed inside a sentence … passes these tests, though its words then name the revision outside a label unit, an identity by the revision's full object id." The identity bullet ends "where it sits is the first limit above". The THEN reads "outside a citation and an excepted identity", and the AND names both. The round-7 fragment (A) still passes every decide-line. Under the new text the THEN is now true of it: R's id appears only inside the excepted identity. The limit states that this placement is undecided. But the THEN still names fewer exceptions than the decide-line excepts (Finding 1). |
| N1 (note) | Question 6's table broken by an interposed note | **Repaired.** Both notes sit below the table (packet lines 303–320), so the two option rows are contiguous. |
| N2 (note) | Residual census at cycle-3 figures | **Repaired.** Delta lines 768–773 give a dated re-measure: "17, 68 and 6". This matches `--check` and my count. |
| N3 (note) | Two cycle-5 wordings guarded only by the digest | **Repaired.** The guards are `DESIGN_PHRASES` line 335 and `REQUIRED_ONCE` lines 198–205. My own mutants are each killed by their own phrase. |

## Criteria

1. **Direction content: met.**
2. **Specification bar: not fully met** (Finding 1). What is decided is still a sweep with a denominator: "The count of those sites is the denominator" and "the occurrence count as this sweep's own denominator". Its falsifier list is still caught by the decide-lines (my fragments C, D and E fail). But scenario 5's THEN is still not carried by the decide-lines.
3. **Contract claims: met.** The coverage, repair-delta and proposal patches are unchanged in substance. RFC4-11.r1 rests on "it never reconstructs commit history it cannot reach", and the totals re-derive.
4. **Signed bytes: met.** Only the two warrant lines are removed, and `--check`'s byte-identity and lost-line guards pass.
5. **Mechanics: met.** All checks pass in the clone, and the census and totals re-derive.
6. **Honest claims: met, with Note 1.** The packet's summary now matches the requirement and lists the status line as an exception.
7. **Plain language: met, with Note 3.**

## Findings

**Finding 1 — Scenario 5's THEN still names fewer exceptions than the decide-line excepts: the operability status line shows R's twelve-digit prefix outside every citation and identity, and passes** (revise)

The scenario reads:

> "**WHEN** a Polaris page has a sentence about the observed revision R outside every label unit **THEN** outside a citation and an excepted identity the sentence shows neither R's full object id nor its first twelve hexadecimal digits"

The decide-line reads "zero swept occurrences outside a label unit and the excepted elements". The requirement excepts four kinds of element, not two. The fourth is "the operability status line that the shared page shell renders on every surface, Polaris included … this requirement excepts it on Polaris and governs nothing else in it."

- [Observed] `page-shell.ts` line 47 renders `` `${status.projectRevision.slice(0, 12)}…` ``, and line 55 places it in `<p class="operability-status" data-human-status …>Eval …; project ${…}; observer …</p>`. Both Polaris pages pass `status` to `pageShell` (`polaris.ts` line 1890, `polaris-source.ts` line 141).
- [Observed] The package says so itself. Packet Question 5 says the status line "shows the revision's short id ("project" followed by twelve hexadecimal digits)". The delta says "on Polaris it shows the observed revision's twelve-digit prefix".
- [Observed, scratch oracle] Fragment B is that line before a label unit. It passes every decide-line I implemented, because the status line is excepted and is also outside the first-occurrence rule. Yet it is text on a Polaris page, outside every label unit, that shows R's first twelve hex digits, and it is neither a citation nor an excepted identity. Its THEN is false, and the oracle passes it.

This is the same defect round 7's Finding 2 held at revise: the THEN lists fewer exceptions than the decide-line does. It sits in a different element. Unlike that route, it is not hypothetical. Every Polaris page renders this line today, and the package discloses it under Question 5. The status line is owner-chosen and disclosed, so it is not itself the defect. The defect is that the scenario's text claims more than its decide-lines decide, which is the brief's test for revise. Butlers-declared verbatim text is a second, theoretical route of the same shape.

[Inferred] A repair that keeps the owner's approach: make the THEN "outside a citation, an excepted identity and the other excepted elements" (or "outside the excepted elements"). Or scope the WHEN to text outside the status line and Butlers-declared text. Neither changes a decide-line.

**Note 1 — The delta's account of the requirement still names only the citation's placement as a limit** (note)

[Observed] `SEMANTIC-DELTA.md` §"What changes", lines 257–259, reads: "Two limits are stated in the requirement and not decided: where the citation sits (one placed inside a sentence passes), and which tokens a served locator holds". The identity bullet just below (lines 260–265) says nothing about placement. The cycle-6 summary at lines 155–162 lists the places it carried the gap to, namely the requirement, the scenario, decision 13 and Question 6, and does not claim this section. So this is an omission, not an overclaim. But a reader of the delta's account would take identity placement as decided. Add "or an excepted identity" to the limit, with a dated mark, as the five-scenarios line at 360–361 has.

**Note 2 — "Where … sits is not decided by this requirement" is broader than true: the first-occurrence rule does decide one placement** (note)

[Observed, scratch oracle] Fragment D is a served identity inside a sentence that comes before the page's first label unit. It **fails** the decide-line "on every Polaris page, the first swept occurrence outside the operability status line inside a label unit". The same holds for a citation's stamp. So the requirement does decide one thing about where a citation or identity sits: neither may hold the page's first swept occurrence. The limit's own words, "passes these tests", are true of the citation and identity tests it follows. The absolute sentence "not decided by this requirement" claims less than is decided, which is the safe direction, so this is not a false limit in the brief's sense. The packet's "either one placed inside a sentence or heading passes" (line 171) has the same breadth. [Inferred] A possible tightening is "…is not decided by this requirement beyond the label-leads rule".

**Note 3 — One unreflowed line in the proposed requirement** (note)

[Observed] `proposed/spec.md.patch` line 58 is 92 columns (`unit, an identity by the revision's full object id. Which tokens an anchor's served`). That is the cycle-6 insertion, left unwrapped in an otherwise hard-wrapped requirement. It is cosmetic. Any reflow changes the spec digest and the `REQUIRED_ONCE` phrase is whitespace-flattened, so do it together with Finding 1's repair, not alone.

Counts: 0 blocking, 1 revise (Finding 1), 3 notes (1–3).
