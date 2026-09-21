# Review — PWB registry currency bounds and briefing ceiling amendment
Reviewed commit: 303066819e8f267136425d0de67e48eeac34e731
Manifest SHA-256: 277a50db35640b8ec9afc031f752b2ff9a724c7db04be9dff98919a54db6bd94
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session. No authoring context; the package was read
for the first time this session, in the order `AGENTS.md`, `REVIEW-BRIEF.md`,
then the artifact. Read-only throughout the worktree; every mutation ran
either through the package's own `structure_findings`/`selftest` functions
invoked directly (no tree write) or in a `cp -r` / manually-constructed
scratch tree under the session scratchpad
(`/tmp/claude-1000/-home-tze-GitHub-syzygy/25dc4c66-2fc9-4594-82e1-b88a40232dcc/scratchpad/review-scratch/`),
never in the reviewed worktree. Commit message bodies were not read. Class:
fresh-reader semantic review of a normative delta (CC-REV-4, CC-REV-6),
against the package's own ten acceptance criteria plus seven additional
criteria (a–g) supplied by the requesting session.

---

## What I ran

1. `git checkout -B review/registry-currency-briefing 303066819e8f267136425d0de67e48eeac34e731`.
   `git status --porcelain` → empty, before and after every step below.
2. `python3 scripts/build_pwb_registry_currency_briefing_amendment.py --check`
   → exit 0: "PWB registry currency-and-briefing amendment manifest matches
   the 1 proposed subject (13 currency bounds, 1 new response ceiling); the
   patch applies to the bound bytes".
3. `--selftest` → exit 0: "subject drift, patch corruption, manifest digest
   and path mutation, version bump, limit semantics, claim-class population,
   bound value, semantics keys and JSON validity all fail closed". I read
   `selftest()` (lines 247–356): ten labeled predicates, each mutating one
   real byte sequence and asserting the mutation differs from the original
   before checking the assertion fails. None is a tautology. See F1 for what
   they do not cover.
4. `--diff` → captured to a scratch file; byte-diffed against
   `proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch` on
   disk with `diff` → **identical**.
5. Manifest digest, computed not transcribed (rule 3): built a scratch tree
   at `…/review-scratch/patched-tree/.syzygy/governance/declarations/adapter-registry/`,
   copied the subject's current bytes in, ran
   `git apply --whitespace=nowarn proposed/*.patch` (exit 0), then
   `sha256sum` on the result →
   `dd2773c065c21d1b5152b89f987aaa28ae29c5294b9bca9eb5203adff1920707`. Equals
   the manifest row exactly. The patched file parses as JSON
   (`json.load` succeeded).
6. Key-level delta, both files parsed and flattened to leaf paths in Python
   (script in scratchpad, not committed): **212 leaf keys before, 247 after,
   0 removed, 2 changed (`registryVersion` and `entries[0].observerVersion`,
   both `1.1.0-candidate.1` → `1.2.0-candidate.1`), 35 added, 210 byte-
   identical**. The 35 additions are exactly: 26 `currencyBounds` row fields
   (13 rows × 2 keys), 7 `currencyBoundSemantics` sentences, and 2
   `resourceLimits`/`resourceLimitSemantics` entries for
   `maxBriefingResponseBytes`. This is acceptance criterion (a), fully
   satisfied: every existing key survives unchanged except the two
   convention-consistent version bumps, and the diff applies cleanly to the
   bound bytes.
7. Structural-claim surface, direct invocation (not through `--selftest`):
   imported the builder module and called `structure_findings()` against
   three mutations `--selftest` does not construct — a bare top-level
   `registryVersion` mismatch (leaving `observerVersion` correct), a
   duplicated `claimClass` between two existing rows, and a zeroed
   `maxBriefingResponseBytes`. All three produced non-empty findings, i.e.
   the checks are real and fail closed; they are simply untested by
   `--selftest` itself. See F1.
8. `python3 scripts/check_governance.py` at the reviewed commit, full output
   read (not just exit code): **32 OK, 20 WARN, 0 FAIL (52 checks)**. The
   package's own files and the new builder script are not named by any
   finding, WARN or otherwise; `pwb-registry-currency-briefing` does not
   appear anywhere in the 765-line output. This corroborates
   `OWNER-DECISION-PACKET.md`'s claim that no `check_governance.py`
   registration is needed yet.
9. Swept the package's four Markdown files for a 64-hex token:
   `re.findall(r'[0-9a-f]{64}', text)` over `IMPACT-LEDGER.md`,
   `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md`, `SEMANTIC-DELTA.md` →
   **0 hits in all four**. Denominator: every `.md` file in the package
   directory (4 of 4). Confirms criterion (e)'s second half.
10. `grep -n "PWB_EFFECT_ACTS\|ADOPT POLARIS BUTLERS"` over
    `scripts/check_governance.py` → the phrase `ADOPT POLARIS BUTLERS
    PROJECT-SHAPE OBSERVER REGISTRY ENTRY` is `PWB_EFFECT_ACTS[2][0]` and is
    reused, unchanged, as `PWB_EFFECT_AMENDMENT_ACTS[1][0]` for the
    2026-09-05 amendment. A further superseding act of the same type over the
    same subject reuses the same registered label. Confirms criterion (e)'s
    first half.
11. Two-method citer sweep, re-run this session at the reviewed commit
    (Python `re` over `git ls-files -z`, UTF-8 decode, versus
    `git grep -l -F`), for three identifiers: `currencyBounds` (8/8),
    `maxBriefingResponseBytes` (12/12), and the subject basename (50/50).
    Both methods agree on all three (rule 2's "confirmed by a second method").
    Total tracked files at the reviewed commit: **1,341** — exactly the
    ledger's stated baseline **1,334 + 7**. I confirmed the "+7" by
    `git diff --name-status a4a34510a5582edbd38c1df57a064ba3ac0a33f2
    303066819e8f267136425d0de67e48eeac34e731`: exactly 7 files added. See F2
    for what that diff shows about the ledger's own breakdown of those 7.
    `currencyBounds`'s baseline-to-reviewed delta (4 → 8) reconciles exactly:
    of the 7 new files, `git grep -l -F "currencyBounds"` names 4
    (`IMPACT-LEDGER.md`, `SEMANTIC-DELTA.md`, the patch, and the builder
    script) — `OWNER-DECISION-PACKET.md` uses the English phrase "currency
    bounds", not the camelCase token, and does not match.
12. Source cross-check for criterion (c): read
    `packages/three-surface-poc-core/src/project-shape-manifest.ts:58-67`
    (`EXTRACTION_CLASSES`, 9 entries, byte-identical to the delta's nine) and
    `project-shape-model.ts` for every `claimId`-constructing call site:
    `sourceClaim` (`claim:source:<path>`, line 367), `itemClaim`
    (`claim:item:<class>:<key>`, 375), `factClaim` (`claim:fact:<fact>`,
    382), `classAggregate` (`claim:class:<class>`, 403),
    `projectAccountOf` (`claim:project-account:<key>`, 430/447), and the
    literal `claim:project-shape` (three call sites: 345, 611, 658). Six
    distinct claimId shapes, exactly as `SEMANTIC-DELTA.md:118` cites. Mapped
    onto the 13 declared classes with **zero set difference**: the 9
    extraction classes absorb the `item`/`class` shapes, `project-fact-
    declaration` absorbs `fact`, `project-account-statement` absorbs the bare
    `project-account:<key>` shape, `source-coverage` absorbs `source`,
    `project-shape` absorbs the literal. See F4 for why PWB-REQ-004, named in
    the requesting brief for this same check, is not itself this
    vocabulary's source.
13. `RFC2-9`/`RFC2-10` read at their defining clause,
    `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md:187-217`
    (located via `DIRECTIVE-REGISTER.md`, rule 8). Compared sentence by
    sentence against the proposed `currencyBoundSemantics` and against
    `assessCurrency`/`CurrencyBoundDeclaration` in
    `packages/cap1-core/src/staleness.ts:33-155`. `boundChange` restates
    RFC2-9's second paragraph near-verbatim ("A currency bound present in the
    tree without an effective owner act does not unblock its class"), neither
    narrowing nor widening it. `undeclaredClass` and `outOfBoundResult` match
    the code's `no-bound-declared` and `stale` (three `basis` values) arms
    exactly, including the reason strings (`NO_BOUND`/`STALE` constants,
    `staleness.ts:24-25`). See F3 for one ambiguity in
    `claimClassAssignment`.
14. `PWB-REQ-006`, read in full
    (`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md:340-`):
    "Final encoded human HTML and machine JSON SHALL each have an explicit
    byte ceiling" — a two-kinds reading, consistent with the delta's
    characterization of the third ceiling as an addition to, not a
    restatement of, the declared envelope.
15. `docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:410-436` (measurements)
    and `:57` (Q2), `:960-973` (slice 3 ceiling), `:1370`/`:1396` (Q2
    recommendation), read for criterion (b). See F5.
16. Swept for the sibling "derived read-only machine view" package: no
    directory under `.syzygy/governance/contracts/candidates/` names it; the
    phrase and `syzygy-dov.22` occur only inside this package's own four
    Markdown files (`git grep -n -F -e "derived read-only machine view" -e
    "syzygy-dov.22"`). Confirms criterion (f): the package correctly treats
    the sibling as not-yet-landed and does not quote or assume its content —
    see F6 for the one open edge this leaves.
17. Re-read `OWNER-DECISION-PACKET.md`'s "Open questions this package did not
    resolve" (five items) against every other file in the package for a
    contradiction. None found: criterion (g) holds — all five stay stated as
    open, including in `SEMANTIC-DELTA.md`'s own `[Inferred]`/`[Unknown]`
    labels on the same points (class-population completeness,
    `status`/`adoptionStatus`).

---

## Findings

### F1 — revise. `--selftest`'s "ten predicates… all fail closed" line materially undercounts what `structure_findings` actually asserts, and the untested assertions are real.

*Anchor:* `scripts/build_pwb_registry_currency_briefing_amendment.py:131-196`
(`structure_findings`) versus `:247-356` (`selftest`);
`OWNER-DECISION-PACKET.md:221-222` ("`--selftest` mutates ten predicates in
turn and requires each to fail closed").
*Rests on:* verification rule 6 ("mutate the input and confirm the check
fails, per predicate, before trusting it — `--selftest` holds the fixtures")
and `REVIEW-BRIEF.md` criterion 3 ("name any predicate the package asserts
that no mutant covers").

`structure_findings` makes at least fifteen distinct assertions (one per
`findings.append(...)` call site). `--selftest`'s ten predicates exercise
six of them: `observerVersion` bump (not the sibling top-level
`registryVersion` bump — a different field, checked by a different `if`),
resource-limit-without-semantics, claim-class population/order, `maxAgeMs`
positivity, semantics-key population, and JSON validity. [Observed, by line
correspondence.]

I invoked `structure_findings` directly (not through `--selftest`) against
three of the untested assertions, each on a real mutation of the proposed
bytes:

- top-level `registryVersion` reverted to `1.1.0-candidate.1` while
  `observerVersion` stays bumped → `["registryVersion is not
  1.2.0-candidate.1: '1.1.0-candidate.1'"]`
- one `claimClass` duplicated (`"principle"` → `"project-account-section"`)
  → `['currencyBounds declares a claim class twice', 'currencyBounds class
  population or order differs from the declared set']`
- `maxBriefingResponseBytes` zeroed → `['maxBriefingResponseBytes is not a
  positive integer: 0']`

All three fail closed correctly — this is not a bug in `structure_findings`
or in `--check`. It is a gap in `--selftest`'s own coverage of it. By
inspection, at least six more assertions are likewise never mutated by
`--selftest`: `entries` population/count ≠ 1, `resourceLimits`/
`resourceLimitSemantics` not an object, `currencyBounds` missing or empty,
a `currencyBounds` row with unexpected keys, `currencyBoundSemantics`
missing or not an object, and an empty `currencyBoundSemantics` sentence
value.

*Repair:* extend `selftest()` with predicates for at least the three I
mutation-tested above (they are the ones most likely to be silently broken
by a future hand-edit of this same file, since `observerVersion` and
`registryVersion` are edited together by convention but checked separately,
and a copy-paste of a `currencyBounds` row is an easy real mistake); note in
the packet that the remaining assertions are covered by `--check`'s
correctness but not by `--selftest`'s regression net, or extend the fixture
list to match `structure_findings`' full surface and update the printed
count.

### F3 — revise. `currencyBoundSemantics.claimClassAssignment` uses the bare label `project-account:<key>` for two structurally different claim-id populations, and the registry entry alone cannot disambiguate them.

*Anchor:* proposed
`entries[0].currencyBoundSemantics.claimClassAssignment`
(`proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch`,
lines ~326-327 of the diff) — quoted in full: "project-fact-declaration
governs the closed count:<class>, catalog-count:<catalog-key> and
project-account:<key> fact families; project-account-statement governs the
six project-account statements".
*Rests on:* `RFC2-9`'s own text that a claim class with no effective
declared bound "does not unblock its class" — which depends on every claim
being assigned to exactly one declared class unambiguously — and the
sentence's own `undeclaredClass` neighbor, which forbids any implementation
default from repairing a missing or wrong assignment.

`packages/three-surface-poc-core/src/project-shape-model.ts` mints **two**
distinct claim-id shapes from the same six `PROJECT_ACCOUNT_KEYS`:
`claim:fact:project-account:<key>` (via `factClaim`, line 382, fed by
`projectAccountFact()` in `project-shape-coverage.ts:360`/`551-563`, whose
own comment calls these "the six project-account facts") and
`claim:project-account:<key>` — no `fact:` infix — (via `projectAccountOf`,
lines 430 and 447, "the six project-account statements"). The proposed
sentence names both populations with the identical shorthand
`project-account:<key>`, once under `project-fact-declaration` and once
under `project-account-statement`, with nothing in the JSON entry itself
(which is the only artifact this sentence lives inside) to tell a reader —
or a future implementer wiring `assessCurrency` calls — that these are two
different `claimId` prefixes rather than one population double-assigned.
Read in isolation, the sentence is at best ambiguous and at worst
self-contradictory.

*Repair:* spell the fact-family member by its full claim-id shape, e.g.
"the fact:project-account:<key> family" or "the six project-account-section
declaration facts (claim:fact:project-account:<key>)", so the distinction
from the bare `claim:project-account:<key>` statement claims is mechanical
from the sentence alone, not dependent on reading
`project-shape-model.ts`/`project-shape-coverage.ts` side by side.

### F2 — note. The impact ledger's own breakdown of "+7 tracked files" miscounts its Markdown component.

*Anchor:* `IMPACT-LEDGER.md:73-75`: "raises the denominator by **7** (five
Markdown files, one manifest, one patch, one builder script — the patch and
script counted as one each)".

`git diff --name-status a4a34510a5582edbd38c1df57a064ba3ac0a33f2
303066819e8f267136425d0de67e48eeac34e731` lists exactly 7 added files: 4
Markdown (`IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
`REVIEW-BRIEF.md`, `SEMANTIC-DELTA.md`), 1 manifest, 1 patch, 1 builder
script — not five Markdown files. The total (7) is right; the itemized
"five" over-states the Markdown count by one and there is no fifth Markdown
file anywhere in the package to attribute it to. Low severity: nothing
downstream reads the itemized breakdown, only the total, and the total is
correct and independently reproduced (see "What I ran" #11).

### F4 — note. PWB-REQ-004 does not define a "claim class" vocabulary; the requesting brief's criterion (c) named the wrong requirement, though the package itself does not rely on it.

*Anchor:* `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md:487-`
(PWB-REQ-004, "Conflicting declarations are disclosed and precedence is
explicit").

`grep -n -F -e "claim class" -e "ClaimClass" -e "claimClass"` over the whole
spec file returns zero hits. PWB-REQ-004 instead closes a different,
finer-grained population — the "project fact" population of `item:<class>`
and `count:<class>` per extraction class plus `catalog-count:<catalog-key>`
and `project-account:<key>`, a "closed twenty-entry family map" — which the
delta's 13 currency classes are a coarsening of (see "What I ran" #12 for
the exact mapping). I verified the 13-class enumeration instead against the
two source files the delta itself names as authority
(`project-shape-manifest.ts`, `project-shape-model.ts`), with zero set
difference. `SEMANTIC-DELTA.md` and `REVIEW-BRIEF.md` both cite
PWB-REQ-006/007, not PWB-REQ-004, as the governing clauses for this block —
correctly, on this reading — so this is a note on the review instructions
this session was given, not a defect in the package.

### F5 — note. The briefing-ceiling rationale in `OWNER-DECISION-PACKET.md` mischaracterizes its own cited measurement.

*Anchor:* `OWNER-DECISION-PACKET.md:71`: "The design work that asked for
this ceiling costed the briefing at roughly 20 KB…"; compare
`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md:433-436`: "The recommended
20 KB ceiling (Q2) is 2.9× the larger composition (20,480 / 7,076) —
headroom, not a tight budget."

The funnel measured the two one-claim briefing compositions at **7,076**
and **5,150** bytes (`:405-410`), then recommended a 20,480-byte ceiling as
roughly **2.9×** headroom over the larger figure — explicitly "not a tight
budget." The packet's "costed the briefing at roughly 20 KB" reads as
though the *measured* cost were ~20 KB; the measured cost was ~7 KB (about
35% of the proposed ceiling), and 20 KB is the deliberate multiple over
that, not the cost itself. The chosen value (20480) is unaffected and
correctly traces to the funnel's own recommendation
(`:1370`/`:1396`/`:965-967`); only the one-line gloss of the rationale
overstates what was measured. `REVIEW-BRIEF.md`'s own carve-out says a
reviewer "may say a value is internally inconsistent with a sentence in the
same file, and should" — this is the adjacent case, a rationale
inconsistent with its own external source.

### F6 — note. The third ceiling's scope sentence is not, on its own words, exact enough to foreclose a fourth kind of body — by the package's own admission, and the sibling package that would close the gap is not yet in the tree.

*Anchor:* proposed `resourceLimitSemantics.maxBriefingResponseBytes`: "…each
authenticated derived read-only machine view response that serves **one
named subject** composed from an evaluation already served under
`maxMachineResponseBytes`…"; `REVIEW-BRIEF.md` criterion 6; `OWNER-DECISION-PACKET.md:160-168`.

I confirmed by sweep ("What I ran" #16) that no sibling package declaring
the "derived read-only machine view" category exists in the tree at this
commit. Until it does, "named subject" is undefined by any accepted or
even-candidate text — the sentence bounds the ceiling to single-subject
views built from an already-served evaluation, but nothing pins what
counts as a "subject" (a single `claimId`, as `POLARIS-M5-AGENT-BRIEFING-FUNNEL.md`'s
worked example assumes, or something coarser). The packet already names
this exact risk ("a ceiling whose sentence names a category no
specification defines would be a ceiling over nothing"), so this is not a
new gap — it is confirmation that the risk is live as of this commit, and
that criterion 6's answer depends entirely on the sibling package's
content, which this package correctly does not assume.

---

## Verdict basis

Every mechanically checkable claim in this package survived independent
re-derivation: the manifest digest, the patch's applicability and JSON
validity, the exact key-level delta (0 removed, 210/212 unchanged, 35
additions fully accounted for), the 13-class vocabulary against its two
cited source files (0 set difference), the `currencyBoundSemantics`
sentences' fidelity to `RFC2-9`/`RFC2-10` and to `assessCurrency`'s actual
return arms, the absence of any 64-hex token in the package's Markdown, the
correctness of the "no registration needed yet" argument against
`check_governance.py`'s current source, a clean 0-FAIL `check_governance.py`
run with the package in the tree, the honest treatment of the undeclared
sibling package, and the five open questions staying genuinely open
everywhere else in the package. No finding here touches the proposed
registry bytes themselves, the manifest, or the act boundary — all six
findings are about supporting prose (F2, F4, F5), one semantics sentence's
precision (F3), and the self-test harness's coverage of its own checker
(F1). F1 and F3 are real enough that I would not carry them into a
superseding act's argument unrepaired, which is why this is CONFIRM WITH
EXCEPTIONS and not a bare CONFIRM; none of the six is blocking, and none
casts doubt on the digest, the class population, or the package's authority
claims.
