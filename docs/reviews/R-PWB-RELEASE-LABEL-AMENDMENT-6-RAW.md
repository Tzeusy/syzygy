# R-PWB-RELEASE-LABEL-AMENDMENT-6 — fresh-context confirmation review, round 6
Reviewed commit: e661dce481c5512642f9f532ba740a7b3d2146a7
Manifest SHA-256: 9cb39438caf580e6a2b8af8758e02e27ef8591b9324c0d2fb7f9b4ece5947002
Verdict: REVISE

## Provenance and method

- **Commit.** Fresh `git clone` of `git@github.com:Tzeusy/syzygy.git` to a scratch directory, then `git checkout --detach e661dce481c5512642f9f532ba740a7b3d2146a7`. All checks below ran in that clone, not in a worktree (rule 7).
- **Manifest digest.** `sha256sum` over `.syzygy/governance/contracts/candidates/pwb-release-label-amendment/PWB-RELEASE-LABEL-AMENDMENT-MANIFEST.txt` in the clone at that commit. It is the digest of the manifest file, not a row inside it.
- **Checks, output read (rule 4):**
  - `build_pwb_release_label_amendment.py --check`: "release-label candidate matches 11 proposed subjects (7 patched); 17 requirements, 68 scenarios; structure, regeneration, contract coverage, sibling classification and pending-patch order verify".
  - `--selftest`: "66 structure mutants, patch drift, an unclassified sibling, the pending patch population, divergent and failing application orders, a colliding companion patch, and the lost-line guard against an independent subsequence count all fail closed on their own predicates".
  - `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
  - `build_polaris_project_wide_contract_coverage.py --check` (current tree): "matches regeneration — 324 clauses represented". The builder's `--check` runs it over the proposed bytes too.
  - `--diff` read in full for the proposed bytes.
- **Census, independently.** [Observed] The signed `spec.md` at this commit has 63 `#### Scenario:` headings; the spec patch adds 5 (`grep -c '^+#### Scenario:'`). 63 + 5 = 68, matching the builder and the ledger's cycle-4 mark ("17 requirements and 68 scenarios, … PWB-REQ-001 now carries six scenarios").
- **My own falsifier oracle (rule 6).** I wrote a scratch script that implements the proposed citation decide-lines literally (citation holds one cite and one stamp; no letter or digit outside them; cite names a served record; stamp equals that record's revision; cite's whitespace-normalized text equals the served locator; no whitespace unless a listed path; no swept occurrence in the cite) plus the "zero swept occurrences outside a label unit and the excepted elements" sweep, and ran it over four hand-built `/polaris` fragments, each with one label unit first. Results:
  - round-5 raw's falsifier page (cite text "Declared project shape of butlers at revision"): **FAILS** — "cite text is not the served locator", "cite text holds whitespace and is no listed path";
  - control, bare twelve-digit id in a sentence: **FAILS** — "occurrence outside unit/excepted";
  - a citation embedded inside the sentence (Finding 1): **PASSES every decide-line**;
  - a phrase-like one-token served locator (Finding 1, the disclosed limit): **PASSES every decide-line**.
- **My own structure mutants (rule 6).** Over `proposed_bytes()` with baseline `structure_findings` `[]`, I applied eight deletions to cycle-4 wording. Six produced **no** content finding, only the `GOVERNING-DEPENDENCIES` digest finding (Note 1); two failed on their own `REQUIRED_ONCE` phrase.
- **Reading scope.** I read: `REVIEW-BRIEF.md` in full; the package files (`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, manifest, `ROUND-5-DISPOSITIONS.md`) and builder sections; `docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-5-RAW.md`; `apps/three-surface-poc/src/polaris.ts` (lines 190–300, 1180–1215 and a grep of citation sites); PWB-REQ-014's anchor-shape clause in the signed spec (lines 1660–1700); grep hits for P-85 in the P-99 and P-98 sign-off records. One read outside the brief's list, disclosed: `apps/three-surface-poc/src/polaris-narrative.ts` lines 102–108 (`provenanceAnchor`), to learn which value is an anchor's served locator. I did not open `ROUND-1-…` to `ROUND-4-DISPOSITIONS.md`, any other raw, or any Butlers content.

## Round-5 findings: are they repaired?

Each repair is judged against the round-5 raw.

| R5 # | Raw's finding | Status at this commit |
|---|---|---|
| F1 (revise) | Cite's visible text free, so "a sentence naming the revision can be cast as a citation, and the text's 'therefore never a stamp' does not follow" | **Partly repaired.** The raw's literal falsifier page now fails (method). But the raw's property — the one the round-4 raw asked for, "a revision id inside a prose sentence, a heading or the shape-identity section is never a stamp" — is still not decided, by two routes: an embedded citation, which nothing discloses, and a phrase-like locator, which the delta discloses but the requirement contradicts. See Finding 1. |
| N1 (note) | Identity exception's population open; "a record of its own" hard to parse | **Repaired in `spec.md`.** "These two are the whole population: an identity of any other record is not excepted." The decide-line and the limb name the same two. Not carried to `design.md` or the delta's account (Note 2). |
| N2 (note) | New wordings guarded only by the dependency digest | **Partly repaired.** The five wordings the raw named are in `REQUIRED_ONCE` (builder 225–240). The cycle-4 wordings repeat the same class (Note 1). |
| N3 (note) | Q5's options still say "Leave it to the POC specification" | **Repaired.** The row reads "**Leave it ungoverned on Polaris** (this version)". The second row now says "changes a component Trajectory and Orrery share", and a dated note keeps the old words (packet lines 232–238). |
| N4 (note) | Stale ledger cells (lines 41, 43) | **Repaired.** Both cells carry dated marks at the cell. The 68-scenario figure re-derives (method). |
| N5 (note) | "changes no … contract-coverage row" | **Repaired.** It now reads "no base matrix row's bytes (one row, `RFC4-11.c4`, is superseded through the repair delta)", with a dated note (delta lines 698–702). |
| N6 (note) | Cycle-3 direction unrecorded | **Dispositioned.** The record named is `OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`. I did not open it, since it is outside the brief's list. |
| N7 (note) | Sibling builders; derived patches do not compose | **Repaired.** The delta's §"Pending siblings" carries a dated mark: no sibling is pending, and derived files "never need to compose". The selftest adds a synthetic pending sibling (`SELFTEST_PENDING`, builder 1135–1174), and `--selftest` reports the order mutants failing closed. Both sign-off records name P-85 as regenerated over them (P-99 line 60, P-98 line 59). |

## Criteria

1. **Direction content: met, subject to Finding 1.** The label leads by an observable rule, the id sits beneath it, moved tags are disclosed, and the untagged form is honest. The departures are named as Q2–Q6.
2. **Specification bar: not fully met** (Finding 1). A sentence the text says "is therefore never a stamp", and that the new scenario's THEN forbids, passes every decide-line. Note 3 is a smaller residual of the same kind.
3. **Contract claims: met.** Nothing moved since round 5 in the coverage, design and proposal patches, and the anchors are unchanged. The delta's new claim "PWB-REQ-014's anchor shape requires a locator and does not fix its values" is true of the signed clause: "Every anchor the machine narrative serves SHALL take one shape: … and its locator." (signed spec, PWB-REQ-014 §"Anchor shape").
4. **Signed bytes: met.** The only `-` lines in `spec.md.patch` are the two warrant lines, and the builder's byte-identity and `lost_lines` checks pass.
5. **Mechanics: met.** Every check passes in a clone, the totals re-derive (capability 35, i.e. 29 + 6 + 0; repair delta 94/78/61/27/6; coverage 629 = 137 + 247 + 245), and the census is 68. One caveat: the claim of guard coverage is overstated (Note 1).
6. **Honest claims: met with exceptions.** Question 6's recommended row and the requirement still overclaim (Finding 1). Two counts are stale (Note 2).
7. **Plain language: met, with Note 2.**

## Findings

**Finding 1 — "A revision id in a sentence … is therefore never a stamp" still does not follow: a citation embedded in the sentence passes, and the disclosed locator limit is contradicted by the requirement itself** (revise)

The proposed requirement (spec patch, provenance-stamp bullet) says:

> "So a stamp's citation holds only a served name with no space in it, or a real path, beside the revision. A revision id in a sentence, a heading or any other running text is therefore never a stamp."

The new scenario says:

> "**WHEN** a Polaris page has a sentence about the observed revision R outside every label unit **THEN** the sentence shows neither R's full object id nor its first twelve hexadecimal digits"

The cycle-4 repair constrains the cite's own text. It does not constrain where the citation element sits. Every citation decide-line is internal to the citation element:

- "no letter or digit in the citation outside the cite and the stamp";
- "every such cite's whole text equal to its record's served locator or path …".

None of them speaks to the block around the citation.

*Route A: embedded citation, undisclosed.* [Observed, scratch oracle] This page passes every decide-line:

```html
<div data-kind="label-unit">Butlers v1.0.23 <code>…full id…</code></div>
<p>Declared project shape of butlers at revision
  <span class="citation">(<cite data-anchor-id="A">git-ls-tree</cite>@<code>1a2b3c4d5e6f</code>)</span>.</p>
```

Here anchor A is served with locator `git-ls-tree` and carries that revision. The sentence reads "Declared project shape of butlers at revision (git-ls-tree@1a2b3c4d5e6f)." It is a sentence about R, outside every label unit, and it shows R's first twelve digits. So the scenario's THEN is false, yet the decide-lines pass.

This is not contrived. [Observed] It is one edit away from today's markup, `polaris.ts` line 1200: `<p…><span …>${statement}</span> <span class="citation">(<cite …>git-ls-tree</cite>@<code …>${revision.slice(0, 12)}</code>)</span></p>`. Lines 263 and 277 likewise place a citation inside the same `<p>`/`<li>` as a prose span.

[Inferred] The legitimate pattern (a claim sentence followed by its provenance citation in the same block) and the falsifier (a sentence that names the revision through its citation) differ only in what the words around the citation mean. So no structural predicate over the citation element separates them without judgment.

*Route B: phrase-like locator, disclosed but contradicted.* [Observed, scratch oracle] A cite `Declared-project-shape-of-butlers-at-revision` beside the stamp passes, when the machine narrative serves that string as the anchor's locator. [Observed] Today's locators are the system's own values (`locator: 'git-ls-tree'`, `polaris.ts` lines 293, 1197; `locator: item.source`, `polaris-narrative.ts` line 107). The delta discloses this honestly:

> "a one-token locator chosen to read as a phrase is not decided here"

(§"Repaired a fourth time", "Named limit"). Question 6's row says the same: "One limit stays … does not fix which tokens".

The disclosure is not sufficient, for three reasons:

- It lives only in the delta and the packet. The normative text states the opposite conclusion ("therefore never a stamp"), and the new scenario asserts it.
- The same requirement already shows the right form for a closed-list gap: "The term list is closed: a paraphrase outside it is not decided by this requirement." No equivalent sentence sits beside the citation rule.
- Question 6's recommended row keeps "A sentence cannot be cast as a cite, so every sentence, heading or identity line that names the revision shows the label instead, or drops the id. The label then leads wherever the revision is named." That is in the same cell as the limit that falsifies it, and it ignores route A entirely.

*Severity.* Judged alone, route B would be a note if the requirement stated it as a limit. Together with route A, the requirement, its scenario and the owner's recommended option all assert a property the oracle does not decide. That is round-5 Finding 1's defect, now reached by placement instead of by cite text, so I hold it at revise (CC-SPEC: scenarios its text carries; a falsifier the oracle catches).

*Proposed repair.* [Inferred] Take the round-5 raw's second option, which round 6 shows is the honest one:

- withdraw "therefore never a stamp";
- reword the scenario's THEN to what the decide-lines check (the citation's contents), not what a sentence shows;
- state both gaps in the requirement in the closed-list form: a citation's placement in running text, and the locator token set, are not decided by this requirement;
- reword Question 6's recommended row to match.

A decidable alternative would be a placement rule, for example that the block holding a stamp holds no other occurrence and the citation is the block's last child. [Inferred] Even that does not stop "…at revision (git-ls-tree@…)." Prefer the disclosure.

**Note 1 — cycle-4 wordings guarded only by the dependency digest; the "every new F1 … wording" claim overstates** (note)

`ROUND-5-DISPOSITIONS.md` says "`REQUIRED_ONCE` holds every new F1 and N1 wording". The delta says it "now holds the new wordings". [Observed] Of my eight deletions over the proposed bytes, these six give **no** content finding, only the `GOVERNING-DEPENDENCIES` digest finding:

- "It holds no occurrence that the text sweep below finds." (requirement);
- ", and holding no swept occurrence" (decide-line);
- "holding no whitespace or equal to a path in the checker's own Git listing," (decide-line);
- the falsifier tail "holds whitespace and is not a path in the checker's own Git listing, or holds a swept occurrence";
- "So a stamp's citation holds only a served name with no space in it, or a real path, beside the revision.";
- the new scenario's body clause "with no whitespace unless it is a path in R's tree," (`NEW_SCENARIOS` guards titles only).

Two deletions were caught by their own phrase: the "whitespace-normalized" clause and the "or it is a path …" sentence. After a later `--write` regeneration, the six would have no content guard. This is round-5 Note 2's class again. Either guard them or narrow the claim to what is guarded.

**Note 2 — the cycle-4 repairs are not carried into `design.md` decision 13 or the delta's account; two scenario counts are stale** (note)

- `design.md` decision 13 (patch) still says "an identity shown whole, equal to the evaluation identity or a served record's own identity". That is the open population round-5 Note 1 closed in the spec. It also says a stamp's cite names "a served anchor or source record carrying that revision, so a sentence or heading never holds one", with no cite-text equality (see Finding 1). The disposition confirms design was not touched: "the capability, design, proposal and contract-coverage patches are as round 5 read them".
- `SEMANTIC-DELTA.md` §"What changes", which "describes this version", still gives the identity as "a served record's own `identity`". Its stamp bullet omits the cite-text rule. It reads "**Four new scenarios.**" and lists four; the patch adds five (method).
- `OWNER-DECISION-PACKET.md` Question 1: "PWB-REQ-001 gains the release label and four scenarios." It gains five.

A reader comparing design, delta and spec meets three populations for one exception (VIS-3).

**Note 3 — "names the observed revision only in a label unit" is swept only at twelve digits** (note)

The prohibition is decided over "the observed revision's full object id, its first twelve hexadecimal digits, or the project's name followed by a captured tag's name". A sentence showing a seven- or ten-digit prefix passes every decide-line. Yet the requirement says "Polaris names the observed revision only in a label unit", and design decision 13 says the checker sweeps "for any other short or full id of the revision". [Inferred] The twelve-digit sweep is a defensible, decidable choice. But either the declarative sentence and the design line should say "as the sweep defines it", or the gap should be stated beside the term-list gap. This was not raised by round 5. I raise it independently, at note level.

Counts: 0 blocking, 1 revise (Finding 1), 3 notes (1–3).
