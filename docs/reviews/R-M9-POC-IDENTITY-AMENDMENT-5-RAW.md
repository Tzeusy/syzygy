# R-M9-POC-IDENTITY-AMENDMENT-5 — fresh-context review, round 5, Three-Surface POC identity amendment
Reviewed commit: e7fd5301daf1c52a8e8ddab08cb1e50ddf4169d8
Manifest SHA-256: 998215c3aad0483f9862432cddfec6e1b263cd69dc5803e6b9c3a1e1f69b391c
Verdict: REVISE

Reviewer: a fresh-context agent that did not draft the package. Scope: the
brief at
`.syzygy/governance/contracts/candidates/three-surface-poc-identity-amendment/REVIEW-BRIEF.md`.

I read:

- the four patches and the manifest;
- `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md`;
- the builder;
- the governing references the brief lists.

For round-4 context only, I also read `ROUND-4-DISPOSITIONS.md` and
`docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-4-RAW.md`, as the dispatcher
directed.

I ran the checks in a fresh `git clone` of the worktree, checked out detached
at the reviewed commit (`.../scratchpad/r5clone`). I applied the patches only
in a separate scratch copy (`.../scratchpad/r5apply`), never in a tree.

Citations written "applied spec.md:N" or "applied CONTRACT-COVERAGE.md:N"
point to the proposed bytes after `git apply` of the four patches in that
copy.

## Verification log

- [Observed] **Commit and manifest digest.** `git rev-parse HEAD` in the
  worktree reads `e7fd5301daf1c52a8e8ddab08cb1e50ddf4169d8`. `sha256sum` of
  `THREE-SURFACE-POC-IDENTITY-AMENDMENT-MANIFEST.txt` (the file) at that
  commit gives `998215c3aad0483f9862432cddfec6e1b263cd69dc5803e6b9c3a1e1f69b391c`.
- [Observed] **Patches apply and match the manifest.** All four patches
  apply cleanly with `git apply --verbose` over a copy of the signed
  `openspec/changes/three-surface-poc-experience/`. `sha256sum` of the six
  resulting subjects equals the six manifest rows. This is a different
  method from the builder's.
- [Observed] **The signed tree is untouched.** `git diff de81d259 e7fd5301`
  restricted to `openspec/changes/three-surface-poc-experience/` is empty.
  The round-4 repair touched only:
  - the package directory;
  - the builder;
  - the new `ROUND-4-DISPOSITIONS.md` content.
- [Observed] **`--check`** exits 0 in the clone: "manifest matches 6
  proposed subjects (4 patched, 2 unchanged); 26 requirements, Part A 78
  clauses over 139 rows; structure, regeneration and the preserved RFC1-26
  row verify". The requirement count is now computed in the success line
  (`len(REQ_HEADING.findall(...))`), not printed as a literal.
- [Observed] **`--selftest`** exits 0: "32 structure mutants, patch drift,
  manifest order and subject drift all fail closed on their own
  predicates".
  - The harness requires two things of each mutant: that it changes bytes,
    and that it yields a finding starting with its own expected predicate.
  - The eight new mutants include each probe that round 4 reported as
    surviving: a reader-notes sentence, the group range, POC-REQ-054's
    renderer independence, POC-REQ-055's "none is imported" and the
    proposal's Q4 sentence.
- [Observed] **`check_governance.py`** in the clone: "32 OK, 21 WARN, 0
  FAIL (53 checks)". No output line names this package's directory
  (`grep -c -F identity-amendment` gives 0). The clone's
  `git status --short --ignored` shows only the gitignored
  `scripts/__pycache__/`. The worktree is clean.
- [Observed] **Dependency file.** In the scratch copy,
  `build_three_surface_poc_spec_dependencies.py --check` passes over the
  applied bytes: "26 requirement(s), 90 distinct authorities".
- [Observed] **Independent recount.** My own Python over the applied matrix
  and spec, importing nothing from the builder, gives:
  - Part A: 139 rows over 78 clauses, 103 covered and 36 Unknown, with no
    third disposition. There are 32 rows marked "Amendment row".
  - Part B1: 28 rows over 27 clauses. Part B2: 219 clauses.
  - Families (A/B1/B2), all equal to the printed table: RFC1 12/4/23, RFC2
    8/0/19, RFC3 0/0/38, RFC4 10/1/21, RFC5 1/15/11, RFC6 13/1/14, RFC7
    12/4/25, RFC8 5/0/27, RFC9 17/2/41. Total 324.
  - The `contracts[]` union over the applied spec is 78 identifiers, equal
    to the Part A clause set.
  - The applied spec has 26 requirement headings and 28 scenario headings.

  My first pass gave B2 = 196. Its row regex missed suffixed identifiers
  such as `RFC2-19(a)`. Corrected to `RFC\d+-\d+[^ |]*`, it gives the
  figures above. I report this per rule 4.
- [Observed] **Signed matrix, line-set difference.** The patch removes 12
  signed lines:
  - the four Part B2 rows for RFC2-25, RFC6-1, RFC6-3 and RFC6-12;
  - the RFC2, RFC6 and Total family-table rows;
  - five computed-figure prose lines.

  These are exactly what the delta's coverage section now names. The bound
  RFC1-26 row ("Relations outside the closed table don't exist; no
  prose-widening | covered | POC-REQ-052") occurs once before and once
  after.
- [Observed] **Signed spec, line-set difference.** The patch removes 21
  signed lines. All of them lie in the six `READER_NOTE_EDITS` reader-notes
  lines, POC-REQ-060's block, or POC-REQ-060's warrants. No other
  requirement block moves (the builder's per-block equality check agrees).
- [Observed] **Anchors re-checked at source:**
  - RFC6-1 at RFC-0006:108, RFC6-3 at :135, RFC6-12 at :263 and RFC6-14 at
    :279;
  - RFC2-24 at `RFC-0002/rendering-vocabularies.md:103` and RFC2-25 at :168,
    with the `asserted-by-worker` row's Authority column "Visible, never
    green, challengeable, never a status input";
  - the design's slice-3 item 3 at `POLARIS-M9-ONE-IDENTITY-FUNNEL.md`
    lines 804–807, which the new Departure 2 quotes correctly.
- [Observed] **Impact-ledger census.** `git grep -lE 'POC-REQ-05[45]'
  8f1fbec7` returns 25 files, partitioned as the ledger says:
  - 3 M9 planning files;
  - 12 package files and the builder;
  - 3 block-provenance files;
  - the register and `docs/README.md`;
  - 4 raws.

  The sum is 3 + 13 + 3 + 2 + 4 = 25.
- [Observed] **Sibling builder.** `build_three_surface_poc_block_provenance_amendment.py
  --check` passes in the clone. It prints the declared mutually-exclusive
  WARN for this package and the governing-intent package.
- [Observed] **My own rule-6 probes.** I ran each one in the clone through
  `structure_findings`, with `GOVERNING-DEPENDENCIES.md` regenerated over
  each mutated spec so that the dependency digest does not catch spec edits
  by accident:

  | Probe | Result |
  |---|---|
  | POC-REQ-054 attribution sentence changed to "by the identity it carries" (first half only) | survived |
  | POC-REQ-054 "and the consistency limb, its link targets and its slots are still checked" deleted | survived |
  | POC-REQ-054 oracle-independence ownership-procedure sentence deleted | survived |
  | POC-REQ-060 "whose two sets of Unknown records by identity must be equal" deleted | survived |
  | POC-REQ-060 Scope reverted to "every epistemic record" | survived |
  | POC-REQ-060 Inferred scenario's "leaves every Unknown in the machine answer Unknown" deleted | survived |
  | RFC6-3 covered row justification narrowed to "each element" | survived |
  | RFC2-25 "Visible" Unknown row deleted | caught (Part A totals) |
  | RFC2-25 "Visible" row flipped to covered | caught (Part A totals) |
  | Signed reader-notes sentence "observation points for every oracle below" edited | caught |

## Round-4 findings: repair check

- **26 (revise) — POC-REQ-054's machine-answer identities and "unowned".**
  Partly repaired. Three parts are fixed:
  - Machine-answer records now enter the Scope, the sweep population, the
    Observable, the decision rule and the falsifier.
  - "Owned" is decided by a stated procedure (applied spec.md:951–954).
  - The two value-free limbs hold for every subject.

  The attribution procedure, which keeps the new limbs non-circular, still
  covers elements only. See Finding 33.
- **27 (revise) — POC-REQ-060's denominator.** Repaired. The Scope
  (applied spec.md:1131–1133), the sweep (1138–1141), the decision rule
  (1157–1158) and the falsifier (1166–1167) all quantify over every entity,
  relationship and claim and require exactly one record. The RFC6-14
  covered row (applied CONTRACT-COVERAGE.md:154) matches.
- **28 (revise) — RFC2-25's limbs.** Repaired.
  - "Visible" has an Unknown row (:115) and "challengeable" has its own
    (:116).
  - "Never a status input" is split into a covered row for the two
    computations (:113) and an Unknown row for positive status (:114).
  - "Never clears an Unknown" moved to :113.

  I note one remaining reading question at :112 (Finding 35).
- **29 (note) — the "every other signed row" sentence.** Repaired. The delta
  says "every other signed consequence or belief row" and names the
  family-table rows and the five `COMPUTED_LINES`. My line-set difference
  agrees.
- **30 (note) — guard gaps.** Repaired for every probe round 4 reported, and
  the requirement count is now computed. New repair text is again partly
  unguarded (Finding 37).
- **31 (note) — Inferred's provenance and "addresses".** Repaired. The
  source limb has an Unknown row (:117). "Each Unknown it addresses" is
  replaced by a recount of every Unknown with and without the record,
  compared as sets by identity.
- **32 (note) — role-pair departure and the split row.** Repaired. Both the
  delta and the owner packet carry "Departure 2 — role pairs", each with the
  design quote and what "Revise" would remove. The semantic-class and rule
  row now sits under RFC1-25 (:94), and "No relation is re-typed" under
  RFC1-26 (:95).

## Findings

**Finding 33 — POC-REQ-054 attributes elements, not machine-answer records, to subjects, yet the RFC6-3 covered row and the delta say it attributes both** (revise)

[Observed] The repair puts machine-answer records into the population. The
sweep enumerates "over the union of the served surfaces and the machine
answer, every element and every record carrying a subject identity"
(applied spec.md:970–972). The new limbs are stated over both. The
Observable says "every element and record attributed to one subject
carries one identity value, and no identity value is carried by elements or
records attributed to two subjects" (applied spec.md:977–979).

[Observed] The procedure that does the attributing was not extended. The
oracle-independence bullet reads: "It attributes each element to its subject
by the source record the element renders, never by the identity the element
carries" (applied spec.md:1003–1005). The ownership test it then states also
speaks only of "the source record the element renders" (1006–1008). The
equality limb is "per-element identity equality … for each owned subject"
(986–987). This requirement's own text distinguishes "element" from
"record" (966–967, 971, 977–979, 986, 991–992), so on its own terms the
attribution rule does not reach records.

[Inferred] **The gap is round 4's Finding 26(a) moved one step.** Nothing
stops a machine-answer record from being attributed by the identity it
carries. Suppose `GET /api/poc` names subject S by a value v′ different from
the value v that the surfaces render:

- The record is attributed to whatever v′ names, which may be no source
  subject at all. So "one identity value per subject" does not fire for S.
- v′ names only that record. So "one subject per identity value" does not
  fire either.
- A phantom subject has no owning source record, so the equality limb
  "makes no claim for it" (1009).

The divergence the required behavior forbids ("every surface and the
machine answer SHALL name that subject by that identity and by no other",
949–950) passes the oracle.

[Observed] **The package says more than the requirement.**
- The RFC6-3 covered row justifies "and in the machine answer" with:
  "POC-REQ-054's oracle attributes each element and record to its subject
  by the source record it renders" (applied CONTRACT-COVERAGE.md:145).
- `SEMANTIC-DELTA.md` §1 says the same: "The checker attributes each
  element and record to its subject by the source record it renders, never
  by the identity it carries."
- The RFC6-1 covered row (:141) claims "One identity per subject on every
  surface and in the machine answer". Its justification is only that the
  records are in the population, which is not enough without attribution.

Criterion 2 is not met: oracle independence does not cover the
machine-answer limb. Criterion 3 is not met: the RFC6-3 and RFC6-1 covered
rows claim a machine-answer attribution that the requirement's oracle does
not state.

Repair: extend the oracle-independence sentence, the ownership test and the
equality limb to "each element and record … by the source record it renders
or answers for, never by the identity it carries". Add a required phrase for
it. Or narrow both covered rows and add an Unknown row for the machine-answer
limb.

**Finding 34 — POC-REQ-054's first scenario states a narrower denominator than its sweep** (note)

[Observed] The sweep's third denominator is "the number of identities that
appear in more than one of the surfaces and the machine answer" (applied
spec.md:973–974). The scenario "One subject, one identity on every surface"
still reports "the number of identities rendered on more than one surface as
its denominator" (1027–1029). The sweep's population was widened by the
repair, but this scenario line kept its round-4 wording. [Inferred]
CC-SPEC's bar asks that scenarios carry the requirement text, so one
denominator phrase should be used in both places.

**Finding 35 — "never green" is read as visual distinctness; RFC2-25's own table uses "green" as a positive status** (note)

[Observed] Applied CONTRACT-COVERAGE.md:112 covers "never green" as "it
renders with the declared Inferred encoding, which the legend distinguishes
from Observed". In RFC2-25's table, the `gate-backed` row's Authority column
lists "green" among positive status claims: "(Aligned, Converged,
reconciled, green)". Row :114 copies that list into the Unknown row for
"never a status input".

[Inferred] On that reading, "never green" is closer to "never rendered as a
positive status" than to "rendered unlike Observed". The oracle also does
not check that the declared Inferred encoding is not itself the positive or
green treatment. This does not reopen Finding 28: the row now quotes the
clause's word and states its reading. But the owner should see that the
covered limb rests on a reading, perhaps through an `[Inferred]` tag on the
row or a sentence in the delta.

**Finding 36 — the ownership procedure's key term is not defined per source** (note)

[Observed] "Owned" is decided by whether "the source record the shared model
reads for the subject carries a non-empty identifier of that source's own
record format" (applied spec.md:952–954). That is a stated procedure, and it
answers round 4's "undefined" objection. But "the identifier of that
source's own record format" is not named for either source the example
gives.

[Inferred] For a Beads work item the identifier is plain: the issue id. For
a code region, the obvious candidates in git's record format are the path,
which RFC6-1 bars as a selection identity (the proposal restates this), and
the blob or tree oid, which changes with content and is not durable. So the
classification step may still need judgment for code regions. Row :142
already lists the surface-local-handle limb as Unknown, and the proposal
defers the identity's form to slice 6, so this is disclosed in substance. A
sentence saying the per-source identifier field is fixed by the slice that
lands the form would close it.

**Finding 37 — the round-4 repair text is partly outside the builder's phrase guards** (note)

[Observed] Seven of my ten probes survived `structure_findings` once the
dependency file was regenerated (see the log). Among them:

- POC-REQ-054's sentence keeping the consistency limb for unowned subjects;
- the ownership sentence in POC-REQ-054's oracle independence;
- POC-REQ-060's "two sets … must be equal" comparison;
- POC-REQ-060's object-based Scope;
- the Inferred scenario's new THEN limb;
- the justification text of an amendment row.

[Inferred] The manifest digest freezes the reviewed bytes, so this is
defence in depth, the same posture as round 4's Finding 30. Criterion 5 is
met: every declared mutant fails on its own predicate.

**Finding 38 — the sibling-package regeneration step sits in the ledger, not in the delta's residual list** (note)

[Observed] `IMPACT-LEDGER.md` now marks its "Sibling packages: none"
sentence stale and says that this package and the governing-intent
amendment (P-100) are mutually exclusive. Whichever is signed second "is
regenerated over the first's applied bytes". The block-provenance builder
prints the same WARN. `SEMANTIC-DELTA.md` §"Residuals the sign-off change
must carry" still lists four items and does not name this step.

[Inferred] The package does name it, so criterion 6 is met. A fifth
residual line in the delta would put it where the signing change will look.

## Criteria summary

1. **Ruling content: met.** [Observed] The package carries:
   - POC-REQ-054 with the ribbon scenario ("A three-state view with nothing
     joined");
   - the POC-REQ-060 amendment;
   - POC-REQ-055;
   - Q3's repair as a new requirement plus a dated disclosure, with the
     bound row preserved once;
   - Q4's typed landing zone with no production constructor.

   Both departures from the adopted design are now labelled for the owner.
2. **The specification bar: not met.** Finding 33: POC-REQ-054's
   attribution procedure, which keeps the machine-answer limb non-circular,
   covers elements only. POC-REQ-055 and the amended POC-REQ-060 meet the
   bar: one form, a scope, a sweep with a denominator, an observable, oracle
   independence, a falsifier, and scenarios carried by the text. Finding 34
   is a scenario wording note.
3. **Contract claims: not met.** Every quoted anchor matches its clause
   [Observed]. The RFC6-3 and RFC6-1 covered rows claim a machine-answer
   attribution that the oracle does not state (Finding 33). Every newly
   listed RFC2-25 limb now has a row (Finding 35 is a reading note).
4. **Signed bytes: met.** [Observed] The tree is untouched. Only the four
   Part B2 belief rows move, plus the computed family and prose lines that
   the delta now names. The RFC1-26 bound row survives byte for byte.
5. **Mechanics: met.** [Observed] `--check` and `--selftest` pass. All 32
   mutants fail on their own predicates. The dependency file equals
   regeneration, the printed totals equal my independent computation, and
   the requirement count is computed. Finding 37 notes guard gaps.
6. **Honest claims: met.** [Observed] The package claims no adoption and
   schedules no implementation. The packet and delta say the repaired bytes
   are unconfirmed pending this round. The three named residuals stand:
   - the sign-off route;
   - the reconciliation checker and census;
   - the recorder registration.

   Finding 38 is a placement note.
7. **Plain language: met.** [Inferred] "What this does not do", the two
   labelled departures and the owner packet's "What you would be signing"
   let a fresh reader restate what changes and what does not.

Counts: 1 revise-level finding (33), 5 notes (34–38), 0 blocking.
