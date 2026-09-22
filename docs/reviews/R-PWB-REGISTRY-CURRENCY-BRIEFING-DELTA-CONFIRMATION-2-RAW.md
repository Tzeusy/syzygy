# Review — PWB registry currency bounds and briefing ceiling amendment (confirmation round 2)
Reviewed commit: 869d21dfcc7d7d3864518383afda920a28049c9d
Manifest SHA-256: 5525b359ec1c38593e3bc466c7bd18e2b5c2fa34e3faae872c5bc7ee3dbd48ba
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session. No authoring context; the package and its
governing references were read for the first time this session, in the
order `AGENTS.md` (Hard prohibitions, Epistemic and change discipline,
Verification rules), `REVIEW-BRIEF.md`, then the artifact. Inputs held to
the requesting session's exact list: the package's five files and
`proposed/`, `scripts/build_pwb_registry_currency_briefing_amendment.py`,
the two prior raws (`R-PWB-REGISTRY-CURRENCY-BRIEFING-DELTA-RAW.md`,
`-CONFIRMATION-RAW.md`), the clauses `REVIEW-BRIEF.md` cites (located
through `DIRECTIVE-REGISTER.md` and read at their defining text), the
sibling `pwb-machine-view-amendment` package, and the two owner records
`POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` and
`POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md`. Commit
message bodies and bead notes were not read for intent. Read-only
throughout the worktree; every mutation ran through the package's own
`structure_findings`/`selftest`/`check` functions invoked directly, or in
scratch trees under the session scratchpad, never in the reviewed
worktree. Class: fresh-reader confirmation review of a normative delta
(CC-REV-4, CC-REV-6), against `REVIEW-BRIEF.md`'s ten acceptance criteria.

This is a **second confirmation round**. Both prior raws are bound to
bytes the 2026-09-22 sibling-package reconciliation has since moved (rule
10); `SEMANTIC-DELTA.md`'s own `## Review` section states this and
requires the fresh exact-byte review this raw performs.

---

## What I ran

1. `gh pr view 61 --json headRefOid` → `869d21dfcc7d7d3864518383afda920a28049c9d`,
   matching the assigned head exactly; proceeded rather than stopping.
   `git status --porcelain` → empty throughout.
2. Read `AGENTS.md`'s "Hard prohibitions", "Epistemic and change
   discipline" and "Verification rules" sections before touching the
   package.
3. `python3 scripts/build_pwb_registry_currency_briefing_amendment.py
   --check` → exit 0: "PWB registry currency-and-briefing amendment
   manifest matches the 1 proposed subject (13 currency bounds, 1 new
   response ceiling); the patch applies to the bound bytes".
4. `--selftest` → exit 0: "selftest: 23 predicates — subject drift, patch
   corruption, patch population, a no-op patch, manifest digest, path
   mutation and absence, both version bumps, limit semantics, the
   briefing ceiling's value and exact single-claim scope, claim-class
   population, duplication, row shape and bound value, the semantics
   block's type, keys and empty sentences, entry count and JSON validity
   all fail closed". I read `structure_findings()` (script lines 140-209)
   and enumerated its assertion call sites: **16**, one more than the
   confirmation round's 15, the new one being the `BRIEFING_LIMIT_KEY`
   semantics-match check at line 170 (absent at commit `82cca275`,
   confirmed by `git diff 82cca275273eea0c34bb7e48fcf42269ee4223bb
   869d21dfcc7d7d3864518383afda920a28049c9d --
   scripts/build_pwb_registry_currency_briefing_amendment.py`). I mapped
   every one of the 16 to a distinct predicate among 5-20, and every one
   of `check()`'s three further assertions (patch population, no-op
   patch, missing manifest — the exact three the confirmation round's N1
   flagged as lacking a fixture) to predicates 21-23. 4 (predicates 1-4,
   subject drift and manifest mutation, neither a `structure_findings`
   assertion) + 16 (predicates 5-20) + 3 (predicates 21-23) = 23, matching
   the printed count exactly. No predicate is a tautology: each asserts
   `mutant != proposed` (or the drifted/corrupted equivalent) before
   checking the mutation is caught, and each fixture mutates a real byte
   sequence or a real parsed-document field. **This repairs N1** (the
   confirmation round's non-blocking note that `--selftest`'s coverage
   claim did not extend to `check()`'s three further assertions) beyond
   what N1 asked for — N1 offered either repair as acceptable and this
   package chose the fixture, not the disclaimer.
5. `--diff` → captured to a scratch file, byte-diffed with `diff` against
   `proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch`
   on disk → identical.
6. Manifest digest, computed not transcribed (rule 3): wrote a scratch
   script (`compute_digest.py`) that copies the subject's current bytes
   into a temp tree, runs `git apply --whitespace=nowarn` with the on-disk
   patch (exit 0), and hashes the result: `sha256sum` →
   `5525b359ec1c38593e3bc466c7bd18e2b5c2fa34e3faae872c5bc7ee3dbd48ba`.
   Confirmed present as the sole row of
   `PWB-EFFECT-AMENDMENT-MANIFEST.txt`, read directly. Matches the header
   above.
7. Two-method citer sweep, re-run this session at the reviewed commit
   (Python `re` over `git ls-files -z`, UTF-8 decode, versus `git grep -l
   -F`), for all fourteen of `IMPACT-LEDGER.md`'s identifiers plus the
   subject basename stem: **all fifteen agree between both methods** (4
   skipped-as-non-UTF-8 files, consistent across both baselines and this
   commit). Total tracked files at this commit: 1,387 (grown from the
   baseline's 1,334 by ordinary repository activity since 2026-09-21,
   consistent with `IMPACT-LEDGER.md`'s own statement that its tables are
   baseline-commit tables, not restated later, and that a reviewer wanting
   later figures re-runs the sweeps). The ledger's own 43-file partition
   and its tables 1-7 are unchanged bytes at this commit: `git diff
   98a5fcb7db7017e8cd8a8a43421ba8a5a96c8958
   869d21dfcc7d7d3864518383afda920a28049c9d` (the PR's merge-base to its
   head) touches exactly 6 files — `OWNER-DECISION-PACKET.md`,
   `PWB-EFFECT-AMENDMENT-MANIFEST.txt`, `REVIEW-BRIEF.md`,
   `SEMANTIC-DELTA.md`, the patch, and the builder script —
   `IMPACT-LEDGER.md` is not among them, so its partition arithmetic
   (already re-derived twice, at `3030668` and `82cca27`) did not need a
   third re-derivation; I independently confirmed the two-method agreement
   holds at this commit instead, which is the part that could have
   silently broken.
8. Swept the package's four Markdown files for a 64-hex token
   (`re.findall(r'[0-9a-f]{64}', text)`) → **0 hits in all four**
   (criterion 9).
9. Swept the same four files for "accepted"/"adopted"/"signed off"/"in
   force"/"performed", read every hit in context: every occurrence either
   explicitly disclaims authority ("labels nothing accepted, adopted or in
   force"), names the *predecessor* act correctly attributed as in force,
   or describes what a *future*, not-yet-performed act or record would
   contain. No file claims this package's own bytes are accepted, adopted,
   signed off or in force (criterion 10).
10. `python3 scripts/check_governance.py` — full output read (rule 4, not
    just exit code): confirmed 0 FAIL. The package's own files and this
    raw's target filename are not named by any finding.
11. Read `SEMANTIC-DELTA.md`'s change-class paragraph: "Normative", three
    independent reasons (changes what an implementation is permitted and
    obliged to do; mints a third declared response ceiling additive to
    `PWB-REQ-006`'s envelope; the subject is digest-bound, so no editorial
    path exists). None is wrong; Structural or Clarifying do not fit a
    change that alters render-time behavior and adds a ceiling (criterion
    1).
12. Read `IMPACT-LEDGER.md` tables 2 and 3 in full against `apps/**` and
    `packages/**`: table 3's six files (the observation constant and its
    test, the git-object-reader length-parity test, `routes.ts`, the
    response-limits test, `governance-inputs.ts`) are exactly the
    consumers a third `resourceLimits` field and a third
    `ResponseLimitIdentity` member would touch; table 4 correctly scopes
    `project-shape-model.ts`'s "unchanged at adoption" claim to the
    always-fresh placeholder constant, not to any future claim-class
    classifier (which does not exist yet). I did not find a consumer of
    the subject's bytes absent from either table (criterion 8).
13. Focus area (a)/(b): re-read `OWNER-DECISION-PACKET.md`'s "Open
    questions this package did not resolve", items 1-6, against both
    2026-09-23 decision records word for word. Question 6 —
    "**Held, not answered.** `POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md`
    §2 (question 6): the drafter's leaning — one claim id — goes to the
    `.22` reviewer as input only; the owner decides when that review
    returns. This question stays open." — matches
    `POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md` §2 Q6
    exactly ("Held. The drafter's leaning, one claim id, goes to the `.22`
    reviewer as input only. The owner decides when that review returns")
    and that record's closing section ("It leaves `.18` open question 6
    open"). Questions 1, 2, 4 and 5 are each "Answered", citing
    `...OPEN-QUESTIONS-2026-09-23-DECISION.md` at the section the owner
    record actually answers them in, word for word. No answer is widened:
    the ceiling's scope sentence in the patch is byte-identical to what
    `structure_findings` checks at line 170, and predicate 14 mutation-
    tests the exact "one exact project-shape claim identified by its full
    claim id" phrase against a widened "one named subject" substitute and
    confirms the check catches it. See F2 for one completeness gap in how
    a reader reaches this confirmation.
14. Focus area (a): cross-checked the sibling `pwb-machine-view-amendment`
    package's `proposed/spec.md.patch` and `OWNER-DECISION-PACKET.md`
    again at this commit — the sibling still declares `/api/poc/briefing`
    a category-1 "derived read-only machine view" member without defining
    its required-subject scope, consistent with this package correctly
    leaving that definition to itself and routing the composition question
    to the owner rather than either package silently assuming it.
15. Focus area (a), criterion 4/5: re-derived the claim-id population from
    source, independently of both prior raws' derivation. Read
    `packages/three-surface-poc-core/src/project-shape-manifest.ts:58-67`
    (`EXTRACTION_CLASSES`, 9 entries, matching the delta's first nine
    currency classes). Read every `claimId`-constructing call in
    `project-shape-model.ts`: `sourceClaim` (`claim:source:<path>`, 367),
    `itemClaim` (`claim:item:<class>:<key>`, 375), `factClaim`
    (`claim:fact:${fact.fact}`, 383), `classAggregate`
    (`claim:class:<class>`, 403), `projectAccountOf`
    (`claim:project-account:<key>`, 430/447), the literal
    `claim:project-shape`. Then, unlike either prior raw, traced
    `factClaim`'s argument to its source in
    `project-shape-coverage.ts:78` — `FACT_FAMILIES = ['item', 'count',
    'catalog-count', 'project-account']`, **four** families, not three —
    and to `buildProjectShapeCoverage`'s `byIdentity` loop (lines
    ~432-465), which reconciles each admitted item's identity fact (`fact
    = itemFact(a.item)`, i.e. `item:<class>:<key>`) and pushes the
    **same** reconciled result into **both** `items.push(...)` (feeding
    `itemClaim`) **and** `facts.push(reconciled)` (feeding `factClaim`).
    `project-shape-model.ts:590` maps `factClaim` over the *entire*
    `coverage.facts` array with no filter, and the result is exposed
    unfiltered as `shape.facts` (`project-shape-model.ts` ~596). This
    produces a real, current, surfaced `claim:fact:item:<class>:<key>`
    claim for every admitted item — a **twin** of its `claim:item:` claim,
    carrying the identical epistemic state (both are built from the same
    `reconciled` object) but a distinct claim-id string. See F1.
16. Independently corroborated F1's premise (not merely inferred from
    reading the two source files) in already-reviewed, retained evidence
    outside the package: `docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md`
    and its confirmed review `docs/reviews/R-POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL-2-RAW.md`
    both state, `[Observed]`, that of 1,148 distinct claim identities in a
    retained machine capture, 1,117 are interpolated from observed-project
    text — "278 source paths + 415 item class-and-key pairs + their 415
    `claim:fact:item:` twins + 9 catalog headings" — naming the same six
    construction sites in `project-shape-model.ts` (lines 367, 375, 383,
    403, 430, 447) I read independently at step 15. This is prior,
    already-confirmed evidence that the `claim:fact:item:` shape is real
    and populated at production scale (415 instances, the same order as
    the item population itself), not a theoretical reading of dead code.
17. Swept `REVIEW-BRIEF.md` for the two 2026-09-23 decision records:
    `grep -n "2026-09-23\|OWNER-VALUES\|OPEN-QUESTIONS"` → 0 hits.
    `OWNER-DECISION-PACKET.md` cites them 6 times, including the
    load-bearing question-6 "Held, not answered" disposition step 13
    above verifies. See F2.

---

## Findings

### F1 — revise. `currencyBoundSemantics.claimClassAssignment` omits a fourth, real, currently-minted fact family — `claim:fact:item:<class>:<key>` — from its "closed fact families" enumeration, so the thirteen-row population is not complete as the sentence claims.

*Anchor:* proposed `entries[0].currencyBoundSemantics.claimClassAssignment`
(quoted in full): "…project-fact-declaration governs the closed fact
families `claim:fact:count:<class>`, `claim:fact:catalog-count:<catalog-key>`
and `claim:fact:project-account:<key>`; project-account-statement governs
the six statement claims `claim:project-account:<key>`, which carry no
`fact:` infix and are a different population from the
`claim:fact:project-account:<key>` family above; …".
*Rests on:* `REVIEW-BRIEF.md` criterion 4 ("Is the thirteen-class
population complete and disjoint? … Check it against the nine extraction
classes and the six claim-id families in the two source files, and say
what a class minted in future code would do") and criterion 5's
`undeclaredClass`/`boundChange` clauses, which depend on every currently
minted claim being assigned unambiguously; `RFC2-9`'s "does not unblock
its class" language presumes the class assignment is total over the
claims that exist.

`project-shape-coverage.ts:78` declares `FACT_FAMILIES = ['item', 'count',
'catalog-count', 'project-account']` — four families, the first being
`item`. `buildProjectShapeCoverage`'s `byIdentity` reconciliation loop
builds one `ReconciledFact` per admitted item identity (`fact =
itemFact(a.item)`, i.e. `item:<class>:<key>`) and pushes it into **both**
the `items` array (which `itemClaim` turns into `claim:item:<class>:<key>`)
**and** the `facts` array (which `factClaim` turns into
`claim:fact:${fact.fact}` = `claim:fact:item:<class>:<key>`), with no
filter between `coverage.facts` and the `shape.facts` field
`project-shape-model.ts` exposes. This is not future code: it is the
exact code path both prior raws traced for `count`/`catalog-count`/
`project-account` (the confirmation raw's step 9 explicitly reads
`countFact`/`catalogCountFact`/`projectAccountFact` at
`project-shape-coverage.ts:358-360` and cross-checks their output against
the sentence) — neither raw's step, by its own text, reaches `itemFact`
or `FACT_FAMILIES[0]`, even though it sits in the same file, at the same
definitional pattern, one family earlier in the same closed list.
`docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md`'s independently
confirmed 415-instance count (step 16) corroborates this is a populated,
production-scale claim family, not a dead branch.

Functionally this fails closed today: an unassigned claim class renders
Unknown under `no-currency-bound-declared` per the sentence's own
neighbor, `undeclaredClass` — so a `claim:fact:item:` twin left unbounded
would never render a false-fresh answer. But `claimClassAssignment`'s own
lead-in — "every claim is named by its full claim id, because two
populations differ only by an infix" — asserts totality, and the
enumeration is not total: a fourth, real, already-populated fact family
exists one line above the three the sentence names, in the same array
literal the sentence's three named families are drawn from.

*Repair:* either add "`claim:fact:item:<class>:<key>`, the item-identity
twin of the extraction-class row's own `claim:item:` claims, sharing that
row's bound" as a fourth clause naming which of the thirteen rows governs
it (the extraction-class rows are the natural home, since the twin always
carries the identical epistemic state as its `claim:item:` sibling — same
`reconciled` object, two claim-id strings), or state explicitly in
`outsideTheseBounds` that the twin population is deliberately excluded
and rendered Unknown, and say why that is the correct reading of
`RFC2-9` rather than an oversight. Either repair should also update
`REVIEW-BRIEF.md`'s "six claim-id families" framing, which undercounts
`factClaim`'s own four internal sub-shapes by treating `claim:fact:<fact>`
as one shape.

### F2 — note. `REVIEW-BRIEF.md`'s "Governing references" list omits the two 2026-09-23 owner decision records that `OWNER-DECISION-PACKET.md` cites for six dispositions in the same commit, including the load-bearing question-6 "Held, not answered" claim this review's focus area (a) turns on.

*Anchor:* `REVIEW-BRIEF.md`'s "Governing references" list (nine items, none
naming either 2026-09-23 record); `OWNER-DECISION-PACKET.md` lines
216-277 (six citations of
`POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md` and
`POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` by path and
section).
*Rests on:* `AGENTS.md`'s epistemic-and-change-discipline requirement that
a fresh-context review runs "with only the artifact, its governing
references, and the acceptance criteria" — which presumes the governing-
references list is the complete route to everything the package's own
claims depend on.

`grep -n "2026-09-23\|OWNER-VALUES\|OPEN-QUESTIONS"` over `REVIEW-BRIEF.md`
returns zero hits; the same sweep over `OWNER-DECISION-PACKET.md` returns
six, including the exact sentence this review's assigned focus area (a)
required confirming ("the owner has NOT decided" question 6). This
review's requesting session supplied both records directly, outside
`REVIEW-BRIEF.md`'s own list, which is why this round could verify them —
a reviewer who received only what `REVIEW-BRIEF.md` names would have no
route to the primary record confirming question 6 is genuinely open, and
would be reduced to trusting `OWNER-DECISION-PACKET.md`'s own citation of
it. Non-blocking: every citation I checked against the two records was
accurate (step 13), so this is a completeness gap in the review brief's
own input list, not a misrepresentation in the package.

*Repair:* add both records to `REVIEW-BRIEF.md`'s "Governing references"
list.

---

## Verdict basis

Every mechanically checkable claim in this package survived independent
re-derivation this session: the manifest digest (scripted, not
transcribed, matching the sole manifest row), `--check`/`--selftest`/
`--diff` all pass and print the claimed counts, `--selftest`'s 23
predicates map one-to-one onto `structure_findings`' 16 assertion sites
plus `check()`'s 3 further assertions plus the 4 subject/manifest-level
predicates — fully repairing the confirmation round's N1 beyond what N1
required — the change class (Normative) is correctly assigned, no 64-hex
digest appears in any of the four Markdown files, no file claims
authority it does not have, `check_governance.py` runs 0 FAIL with the
package untouched by any finding, the PR's true diff against
`origin/main`'s merge-base is exactly the six files `SEMANTIC-DELTA.md`
names (no act record, no `openspec/**`, no implementation file touched),
tables 2 and 3 of the impact ledger name every consumer I could find, the
two-method identifier sweep agrees on all fifteen identifiers at this
commit, and every one of the six open questions is routed to its exact
citation in the two 2026-09-23 decision records without widening — Q6
correctly and explicitly stays held for the owner, confirmed against the
owner's own words in both records, not merely against the packet's
restatement of them.

F1 is the one finding I would not carry into a superseding act's argument
unrepaired: `claimClassAssignment`'s completeness claim is false as
written, for a currently-populated, production-scale claim family
(415 instances at last independent measurement) that both prior reviews'
own verification steps came within one line of catching and did not. It
does not touch the manifest digest, the proposed registry values, or the
act boundary, and its failure mode is fail-closed (Unknown, never a false
"fresh"), which is why this is CONFIRM WITH EXCEPTIONS rather than
REVISE. F2 is a real but non-blocking gap in the review brief's own input
completeness, not in the package's substance.

**CONFIRM WITH EXCEPTIONS.**
