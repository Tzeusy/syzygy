# Review — PWB scoped epistemic attributes amendment (round 2)
Reviewed commit: b89e7c7417ba04ccd4d683b7ae939934f348a58b
Manifest SHA-256: 7d9bcdb2aa5145b63b63b8729564996aab4abeadaba3e229c02739dc0caf9206
Verdict: REVISE

Reviewer: fresh-context session. No authoring context; the package was not
read before this review. Read-only throughout; every mutation was performed
in a `cp -r` scratch copy under the session scratchpad, never in the reviewed
worktree. Class: fresh-reader semantic review of a normative delta (CC-REV-4,
CC-REV-6).

Disclosure, so the reader can discount it: one `git show HEAD --` invocation
used to check a claim about `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`
printed the commit message body, which the brief told me not to read for
intent. I had no way to unsee it. No finding below rests on it; every finding
is anchored to file bytes I read directly, and I did not read any other
commit message body.

---

## What I ran

All read-only unless noted; the scratch copy is
`…/085cd76b-…/scratchpad/apply-test` (a `cp -r` of the reviewed worktree).

1. `git rev-parse HEAD` → `b89e7c7417ba04ccd4d683b7ae939934f348a58b`.
   Matches the brief. `git status --porcelain` → empty.
2. `sha256sum PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` →
   `7d9bcdb2aa5145b63b63b8729564996aab4abeadaba3e229c02739dc0caf9206`.
   This equals the argument quoted in `OWNER-DECISION-PACKET.md:19` and
   `:133`. Digest computed, never transcribed (rule 3).
3. `python3 scripts/build_pwb_scoped_attributes_amendment.py --check` →
   exit 0, "manifest matches 11 proposed behavior subjects (3 patched, 8
   unchanged); the contract patch applies to both identical RFC-0007 mirrors".
4. `--selftest` → exit 0, "closed population, byte drift, path order, subject
   drift, patch corruption, contract mirror drift and contract patch
   corruption fail closed". I read the fixture body (`selftest()`, lines
   235–303): seven predicates, each mutating a real input and asserting
   failure. Rule 6 satisfied for the builder.
5. `--diff` → four patches printed, in this order: `GOVERNING-DEPENDENCIES.md`,
   `design.md`, `spec.md` (behavior), then
   `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`
   (contract). The contract patch is printed by `--diff` but is not a manifest
   row — consistent with the package's own statement.
6. Fail-closed probes, exit codes read (rule 4):
   - bare run → exit **2**, "refusing: regenerating the manifest changes the
     act argument; pass --write…"
   - `--apply` without `--at-adoption` → exit **2**, "refusing: --apply writes
     the proposed bytes into the tree and is the adoption step…"
   - manifest drift (first row byte changed, scratch copy) → `--check` exit
     **1**, "manifest differs from exact regeneration over the proposed bytes".
7. `python3 scripts/check_governance.py` at the reviewed commit → output read
   in full, not the exit code: **32 OK, 20 WARN, 0 FAIL (52 checks)**. Checks
   that see this package: CG-7d (`[subject] SIGN OFF PWB SCOPED-ATTRIBUTES
   AMENDMENT — 1 quotation(s), 0 finding(s), 0 performed digest(s)`), CG-7e
   (the packet registered as a digest-copy file), CG-26 ("published battery
   and hosted battery are one list — 28 published, 28 hosted, 28 shared", so
   the two new builder steps are in both).
8. Rule-6 mutation on the registration, in the scratch copy: replaced the
   packet's digest with sixty-four zeros → **FAIL CG-7d** and **FAIL CG-7e**,
   each naming `OWNER-DECISION-PACKET.md` (CG-7d at line 133). The
   registration fails closed before the act exists, as claimed.
9. Contract patch, scratch copy: `git apply --check` against
   `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md` → OK;
   the same patch path-rewritten to `contracts/candidates/rfcs/…` → OK. Before
   the patch both mirrors hash
   `d4ab9646269e4f22274f46ecc9687ac321572372d62a0f30a96a66e306edb9fa`; after
   applying to both, both hash
   `49ce7109cd1d8a809c3da2f8e8f36fb531a4f0102ce39c904c788c4f2558b53a`.
   Identical before and after. Criterion 5's "applies identically to both
   RFC-0007 mirrors" **verified**.
10. Behavior patches, scratch copy: applied all three, then
    `grep -v '^#' PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt | sha256sum -c -` →
    **11/11 OK**. The manifest hashes exactly the post-apply bytes.
    Criterion 7's first limb **verified**.
11. In the same fully-applied scratch copy (behavior + both contract mirrors):
    - `python3 scripts/check_governance.py` → **29 OK, 20 WARN, 3 FAIL**:
      `CG-7a` 1 finding, `CG-7h` 9 findings, `CG-18` 2 findings. This
      reproduces `SEMANTIC-DELTA.md:56-58` exactly (1, 9 and 2). That claim
      **holds**.
    - `python3 scripts/build_polaris_project_wide_spec_dependencies.py --check`
      → "Polaris dependencies match regeneration — 17 requirement(s)". The
      `GOVERNING-DEPENDENCIES.md` patch is an exact regeneration and the "17
      requirement(s), 96 distinct authorities" header is true post-apply, so
      the delta's "No warrant list changes" **holds** mechanically.
    - `python3 scripts/build_polaris_project_wide_contract_coverage.py --check`
      → "Polaris consequence matrix matches regeneration — 324 clauses
      represented". The signed coverage matrix survives, as the delta says.
    - `python3 scripts/build_directive_register.py --check` → prints
      "FAIL: DIRECTIVE-REGISTER.md is stale; regenerate it", **exit 1**
      (the printed line and the exit code agree here; I checked both).
12. Citer re-derivation, both methods, both commits (see F1/F2 for the
    numbers). Method 1: Python `re` over `git ls-tree -r --name-only -z <rev>`,
    decoding each blob as UTF-8 and skipping undecodable ones, patterns
    `PWB-REQ-0(?:07|14)(?![0-9])|PWB-REQ-020(?![0-9])` and `RFC7-33(?![0-9])`.
    Method 2: `git grep -l -F` per literal identifier at the same rev, union.
    Denominators are the `git ls-tree` file counts, computed not asserted.
13. Baseline clauses read at their register-named sites (rule 8): `VIS-1`
    (`doctrine/vision.md`:82), `VIS-2` (:96), `VIS-4` (:122), `VIS-7` (:183),
    `CC-REV-2/4/6` (`review-and-documentation.md`:52/94/120), `CC-TEST-5/6`
    (`testing-and-verification.md`:106/121), `RFC6-22/23`
    (`RFC-0006-…md`:390/404), `RFC7-16` (`RFC-0007/narrative-contract.md`:316),
    `RFC7-33` (`RFC-0007/rendering-and-surface.md`:205), and — not in the
    brief's list, but see F3 — `RFC7-34` (same file:241) and `PWB-REQ-016`
    (`spec.md`:864).

Note on `DIRECTIVE-REGISTER.md`: it lives at the repository root, not at
`.syzygy/governance/DIRECTIVE-REGISTER.md`. My first lookup hit ugrep's
"No such file" for every identifier; rule 1 and rule 4 both say to read the
output, and I did.

---

## Findings

### F1 — blocking. The ledger's re-derived citer count at the reviewed commit is wrong, its enumeration is incomplete, and its universal claim about the additions is false.

*Anchor:* `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/IMPACT-LEDGER.md:24-35`.
*Rests on:* verification rules 2 and 9 (a figure over a denominator needs the
sweep run this session, by a second method, with remainders enumerated); VIS-2
(a stated `[Observed]`-class figure that is wrong is not honest rendering);
the ledger is the artifact the owner is sent to for downstream reach (P-68 row
names it).

The bytes say:

```
At the commit that carries this draft the same two sweeps return
**87 files** over **1,227**; every file beyond the baseline 80 is this
package's own or its retained review, none is an implementation site, and
the table below stays the baseline table:
```

followed by seven bullets.

Re-derived at `b89e7c7`, both methods agreeing:

| sweep | ledger says | I measure | denominator |
|---|---|---|---|
| PWB-REQ-007/014/020, baseline `a9f671e` | 80 / 1,216 | **80 / 1,216** | agrees |
| PWB-REQ-007/014/020, at `b89e7c7` | 87 / 1,227 | **88 / 1,227** | denominator agrees |

The eighth addition, omitted from the seven bullets, is
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` — the P-68 row added
by this same commit, which contains one occurrence each of `PWB-REQ-007`,
`PWB-REQ-014` and `PWB-REQ-020` (counted with `grep -o -F | sort | uniq -c`).
`git grep -l -F` is a substring match and therefore the most permissive of the
three methods; it returns 88 as well, so this is not a pattern artefact.

Three defects in one sentence: the number is wrong by one; the enumeration is
short by one; and "every file beyond the baseline 80 is this package's own or
its retained review" is a false universal — `PENDING-OWNER-DECISIONS.md` is
neither. (The sub-clause "none is an implementation site" remains true.)

This is the second occurrence of the defect class round 1 raised as F13 ("the
80/1,216 figure does not hold at the commit that publishes it"). The repair
added a second, commit-dated figure, and the second figure is itself wrong at
the commit it names — for the same reason: the pass that publishes the figure
is still editing the population it measures. AGENTS.md records the general
lesson ("An absence figure over a population the current pass is still editing
has to be re-derived, never read"), and it applies here.

*Resolution:* re-derive at the exact commit that will be reviewed and publish
88 / 1,227 with all eight additions enumerated, or state the predicate so the
figure is stable under its own publication (e.g. "88 over 1,227, of which 8
are this package's own files, its retained review, and the P-68 register
row"). Do not publish a figure the package's own next edit invalidates.

### F2 — blocking. The RFC7-33 citer sweep is wrong by two, and the class table that sums to it is therefore wrong in two rows.

*Anchor:* `IMPACT-LEDGER.md:184-209` (the sweep sentence at :189, `Sum: 75` at
:209), and the file table at :211-287.
*Rests on:* verification rules 2 and 9; criterion 5 and criterion 6 both make
the owner rely on this list to know what a contract act reaches.

The bytes say "agree on **75 files** over **1,227**". Both methods return
**77** at `b89e7c7` (68 at the `a9f671e` baseline). The two files present in
the population and absent from the ledger's 75-row table are:

- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/IMPACT-LEDGER.md`
  — the ledger itself, which contains seven occurrences of `RFC7-33`;
- `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` — three
  occurrences, in the P-68 row.

No file is in the table and absent from the population, so the error is purely
omission. The class table (`| class | files | disposition |`) sums to 75 by its
own rows, so it needs two rows changed as well as the headline figure: the
ledger belongs under whatever class its five siblings take (the table already
classes `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md`, `SEMANTIC-DELTA.md` and
`proposed/design.md.patch` as "generated index or candidate record"), and the
pending register is a new class or an existing one.

The self-reference is the interesting half: a ledger that cites the identifier
it sweeps for makes itself a member of its own population, so an enumeration
written before the final edit can never close. That is a reason to state the
predicate, not a reason to leave the number wrong.

*Resolution:* publish 77 / 1,227, add the two rows, and correct the two class
counts so they still sum to the headline. State the predicate (whether the
package's own files are in or out) so the next editor can re-derive rather
than re-read.

### F3 — blocking. The package never examines PWB-REQ-016 or RFC7-34 — the non-visual requirement and the clause that sits beside the one it patches — and marks the accessibility oracle "no change expected".

*Anchor:* the absence is the finding. `grep -rn -F -e 'PWB-REQ-016' -e
'RFC7-34' -e 'accessib' -e 'keyboard' -e 'screen reader'` over the whole
package directory returns exactly one line:
`IMPACT-LEDGER.md:79 | apps/three-surface-poc/src/polaris-accessibility.ts |
renderer / model | 0 | 0 | 1 | — |` — i.e. the accessibility renderer is
listed with "no change is expected of the file by this package or its
implementation" (`IMPACT-LEDGER.md:57-59` defines `—` that way). Neither
identifier appears anywhere in `SEMANTIC-DELTA.md`,
`OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md` or any patch.
*Rests on:* `PWB-REQ-016` (`spec.md`:864-883) and `RFC7-34`
(`rendering-and-surface.md`:241-245).

PWB-REQ-016's invariant, quoted:

```
Every project distinction and summary-to-source path SHALL be recoverable by
text and operable by keyboard without relying on color, position or layout.
```

its oracle: "compare the complete interactive/path population to keyboard and
accessibility-tree traces"; its falsifier: "a color/layout-only distinction,
unreachable target, …"; its primary warrant is **RFC7-34**.

RFC7-34, quoted:

```
**RFC7-34 — Non-visual recoverability.** Every such distinction is recoverable
**without colour, position, or layout** — by label, text, or structure; …
```

The amendment's whole mechanism is that a claim's value stops being on the
claim and starts being recoverable only from an *ancestor element* — that is,
from containment. RFC7-34 admits "structure" as a carrier, so I believe the
permission survives RFC7-34; PWB-REQ-016's own wording drops "or structure"
and says "recoverable **by text**", which is the narrower formulation and the
one an oracle author implements. Which of the two governs a scope-carried
tuple field on the accessibility tree is exactly the question the package must
answer, and it does not raise it.

The consequences are concrete and each is asserted in the package without
argument:
- `SEMANTIC-DELTA.md` "What explicitly does NOT change" lists
  PWB-REQ-011/015/016/021/022 as untouched. PWB-REQ-016 is not *patched* —
  true — but the population its falsifier ranges over changes, and the delta
  offers no reasoning.
- The Warrant section lists VIS-1, VIS-2, RFC6-22, RFC6-23, RFC7-16, CC-TEST-5
  and CC-TEST-6. RFC7-34 — the sibling clause, cited as "RFC7-33/34" at six
  separate sites inside the very module being patched (lines 43, 58, 158, 283,
  409 and the §3.11 heading) — is absent.
- `polaris-accessibility.ts` is marked `—`, which the ledger defines as "if the
  bead finds one, the ledger is wrong". On the face of it the bead will find
  one.
- `OWNER-DECISION-PACKET.md:99-102` frames the reader risk as "a reader of the
  raw HTML who does not expand scopes". A screen-reader user is not a raw-HTML
  reader, and the mitigation offered ("the page's claim-states lede would
  restate it") is a prose lede, which is not what an accessibility-tree trace
  reads.

*Resolution:* add a subsection to `SEMANTIC-DELTA.md` stating, against the
quoted text of PWB-REQ-016 and RFC7-34, whether a scope-carried field is
"recoverable by text" for the accessibility-tree oracle; add RFC7-34 to the
Warrant list (or say why it is not warranted on); reclassify
`polaris-accessibility.ts` if the answer is that the renderer must carry
something extra; and say in the owner packet, in one sentence, what a
non-visual reader gets. Do not leave the question for the implementation bead:
PWB-REQ-016's falsifier is release-blocking and the owner is being asked to
authorize a contract act on the strength of this analysis.

### F4 — non-blocking. The strict scope precondition has no falsifier in the over-hoist case; a scope may assert a value false for a member and both oracles stay silent.

*Anchor:* `proposed/spec.md.patch:14-21` (the rule) and `:48-54` (the
falsifier); `SEMANTIC-DELTA.md` "Proposed meaning" carries the same bytes.
*Rests on:* CC-TEST-6 (`testing-and-verification.md`:121-130, "Happy-path-only
coverage of an epistemic surface is a finding … at elevated severity"); VIS-2.

The repaired rule is strict, and that repair is good:

```
A scope SHALL be one element carrying a
machine-readable scope marker, SHALL carry a field only when every claim
under it has that value in the machine answer, and contributes no tuple of
its own after expansion. Where claims under one element differ in a field,
that element carries nothing for the field and each claim carries it itself;
```

But the inheritance sentence two lines above is still written as "a claim's
value for a field it does not carry **itself**", which keeps the case where a
claim under a field-carrying scope carries its own value. Take scope `S` with
`label=Verified`, ten claims under it, nine carrying nothing and one carrying
`label=Unknown` itself. The second SHALL is violated (S must then carry
nothing). Now run the falsifiers:

- PWB-REQ-007's new clause fires on "a claim's expanded value for any field
  differs from the value the machine answer carries for that claim". The
  outlier's expanded value is its own `Unknown`, which is what the machine
  answer carries. It does not fire.
- PWB-REQ-020's fires on a marker "hidden behind a scope value". Nothing is
  hidden; the outlier's marker is present. Both clauses also say the scope
  "contributes no tuple / no marker of its own after expansion", so the scope's
  over-broad value is deliberately invisible to the comparator. It does not
  fire.

So the scope element asserts `Verified` over a population containing an
`Unknown`, in violation of the clause's own SHALL, and no oracle in the package
can tell. This is the residual half of round 1's F3 — that review named it
("a scope marker is then a population-level assertion that is false for a
member … no falsifier of its own") and its strict-branch resolution said to
keep the override sentence "**only as the falsifier's condition-of-violation**".
The repair took the strict branch but did not carry the sentence into the
falsifier. I rate it non-blocking rather than blocking because criterion 3 asks
for "a finite falsifier for a scope **hiding** a differing member" and that one
now exists and is well defined; this case is over-assertion, not hiding, and
per-claim truth survives.

*Resolution:* add to PWB-REQ-007's falsifier a predicate over the scope rather
than the claim — e.g. "a scope carries a field for which any claim under it
carries a different value in the machine answer" — which is finite, decidable
from the machine answer plus the rendered scope markers, and imports no
rendering code. Name the corresponding mutant in PWB-REQ-020's mutation proof.

### F5 — non-blocking. The contract act's downstream regenerations are not enumerated; as planned, a performed contract act leaves three governance checks red.

*Anchor:* `SEMANTIC-DELTA.md` "Migration and supersession plan" step 3 (the
contract successor: "a recorder …; a history entry …; a successor manifest;
the seam extended; a packet with one phrase"); `IMPACT-LEDGER.md:184-209`.
*Rests on:* criterion 5 and the verification-rule-4 discipline (read the
check's output, and check its denominator against the whole population).

I applied the contract patch to both mirrors in the scratch copy and ran the
battery. Three artefacts go stale and only one of them is named anywhere:

| artefact | check | named in the package? |
|---|---|---|
| `.syzygy/governance/contracts/candidates/ACTIVE-CONTRACT-MANIFEST.txt:27` | `FAIL CG-7a` — "rfcs/RFC-0007/rendering-and-surface.md digest 49ce7109cd1d… != manifest d4ab9646269e…" | only obliquely, as "a successor manifest" |
| `DIRECTIVE-REGISTER.md` | `build_directive_register.py --check` exit 1, and the step is in `.github/workflows/governance-docs.yml:127` and the published battery (`PROJECT-STATUS.md:255`) | yes — `IMPACT-LEDGER.md:251`, but see below |
| `.syzygy/governance/contracts/candidates/fixtures/context-selection-8-openspec-authoring.md` | `FAIL CG-18` — stated packet digest and word count (25,029 vs 25,179) both recompute differently | **no — named nowhere in the package** |

The fixture is invisible to the ledger's method by construction: both sweeps
match on the *identifier* `RFC7-33`, and the fixture and the active manifest
cite the module by **path**. A sweep whose predicate is the identifier cannot
find the citers that name the file, and the ledger does not say so.

Separately, the one disposition that is given is wrong in its detail.
`IMPACT-LEDGER.md:203` says of the register: "RFC7-33's definition line moves
by the insert". It does not — the insert lands after line 217 and RFC7-33 is
defined at 205, unchanged. What moves is every clause *after* the insert:
`RFC7-34` 241 → 256, `RFC7-35` 261 → 276, `RFC7-40` 416 → 431. The conclusion
(the register must be regenerated) is right; the stated reason is false.

*Resolution:* add to the migration plan's step 3, by name, every artefact the
contract act must regenerate in the same change — `ACTIVE-CONTRACT-MANIFEST.txt`,
`DIRECTIVE-REGISTER.md`, and
`fixtures/context-selection-8-openspec-authoring.md` — and state the
denominator that found them (a path-based sweep over the module path, not an
identifier sweep). Correct :203 to say that clauses after the insert point
move.

### F6 — non-blocking. The packet's decisive claim for option (a) is a bare categorical resting on an explicitly Inferred, unmeasured estimate.

*Anchor:* `OWNER-DECISION-PACKET.md:112-113`, "This is the only path that meets
the target you set without cutting items." Repeated verbatim in the register
row, `PENDING-OWNER-DECISIONS.md:194`, as "(recommended: the only path that
meets the target without cutting items)".
*Rests on:* AGENTS.md §"Epistemic and change discipline" (label substantive
claims `[Observed]` / `[Inferred]` / `[Unknown]`; an LLM assertion is
Inferred); VIS-2.

Eleven lines earlier the same page says the saving is "about 350 KB
[Inferred — the funnel estimate minus its attribute share; the lane A page has
not been measured with scopes, and the number is confirmed only by the
implementation bead's measurement]". The arithmetic that makes option (a) meet
the target is 1,478,637 − 350,000 ≈ 1,130,000 against a 1,400,000 target — I
checked it and it is right *given the estimate*. But the 350 KB is derived from
the **pre-lane-A** capture and applied to the **post-lane-A** page with no
adjustment, which the delta states plainly (`SEMANTIC-DELTA.md` §Why,
"[Inferred; not yet measured on the lane A page]") and the packet does not. If
the realised saving is, say, 80 KB, option (a) does not meet the target either,
and the categorical is false.

The margin arithmetic for option (b) I also checked and it holds:
1,484,487 + 443,000 = 1,927,487, inside 2,097,152. The "about 612 KB of
headroom" figure is the tailnet form in decimal KB (2,097,152 − 1,484,487 =
612,665); the direct form gives 618,515. Quoting the smaller of the two is the
conservative choice and I raise no finding on it.

*Resolution:* label the claim, and condition it: "[Inferred] on the 350 KB
estimate holding; if the implementation bead measures materially less, (a) does
not reach the target either and the target question returns." Carry the same
qualification into the P-68 row, which is a default-path file.

### F7 — non-blocking. RFC7-33's unedited opening paragraph becomes false for the interactive surface, inside the same clause, by this patch's own design.

*Anchor:* `proposed/contract/RFC-0007-rendering-and-surface.md.patch:9-22`
(the inserted paragraph) against `rendering-and-surface.md:205-217` (the
opener, unedited); `SEMANTIC-DELTA.md` "What explicitly does NOT change",
"RFC7-33's opening paragraph is not edited, only followed by the new one."
*Rests on:* verification rule 8 ("Anchor a contract claim to a defined clause
and quote it; nearby prose is not the clause").

The opener, quoted, is an unqualified universal:

```
… label + tier + reason + freshness — is carried as a
**machine-readable attribute on the rendered unit**, served identically
through the machine-queryable endpoints (RFC6-13/14) and preserved in
plain-text or exported renderings …
```

After the patch, a reader who cites RFC7-33 by quoting its opening paragraph —
which rule 8 tells them is the right thing to do — gets a sentence that is no
longer true of the interactive surface, with no marker in that paragraph
pointing at the exception. The later paragraph is explicit and well scoped
("On the interactive human surface only … in place of on each unit"), so a
reader of the whole clause is not misled; a reader of the clause's first
paragraph is. AGENTS.md records at length what this repository has learned
about false sentences that cannot later be corrected — and once the contract
act binds these bytes, this one cannot be.

A four-word insert-only addition to the opener ("… on the rendered unit, except
as permitted below, served identically …") would keep the patch insert-only and
close it. I record it as non-blocking because "smallest change" is a defensible
reading of criterion 5 and the exception is genuinely explicit.

*Resolution:* extend the insert to add an exception marker to the opener, or
state in the delta, in one sentence, the deliberate choice to leave a
now-partial universal standing and why that is preferable.

### F8 — editorial. The contract paragraph's precondition is looser than the specification's, in the one document that outranks it.

*Anchor:* `proposed/contract/RFC-0007-rendering-and-surface.md.patch:16`,
"A scope never carries a value that any unit under it **lacks**", against
`proposed/spec.md.patch:15-16`, "SHALL carry a field only when **every claim
under it has that value** in the machine answer."

"Lacks a value" is not the same predicate as "does not have that value": a unit
carrying `Unknown` does not obviously *lack* `Verified`. The contract defers
the rule's statement to "an inheritance rule the governing specification states
once", so the strict spec rule governs and nothing is actually loosened — but
the contract is the higher authority and outlives this specification, and it
should carry the predicate it means.

*Resolution:* "A scope never carries a value that is not the value of every
unit under it."

### F9 — editorial. `SEMANTIC-DELTA.md:47` names a baseline commit that is two commits behind the reviewed one, without saying the subjects are unchanged between them.

*Anchor:* `SEMANTIC-DELTA.md:47`, "Baseline: commit
`a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d` (main)"; same at
`IMPACT-LEDGER.md:5`.

I verified `git rev-parse a9f671e` matches, that `b89e7c7`'s parent is
`9098b0b` whose parent is `a9f671e`, and that neither intervening commit
touches any of the eleven behavior subjects or the RFC-0007 module — so the
patches apply at both revisions and the baseline is sound. But the reader is
left to establish that themselves, and the ledger's second figure is stated at
a *different* commit from its baseline, which is part of how F1 went wrong.

*Resolution:* add "; none of the eleven subjects or the RFC-0007 module changes
between this baseline and the reviewed commit" to both lines.

---

## Criteria with no finding

- **Criterion 1 (contract/inheritance rule stated once and complete).** The
  rule is stated once, in PWB-REQ-007, and restated by reference everywhere
  else (RFC7-33's paragraph says "the governing specification states once";
  design decision 9 restates it; PWB-REQ-020 says "the PWB-REQ-007 inheritance
  rule"). All four limbs are present: nearest enclosing scope; absent when no
  scope carries the field, which the falsifier forbids; the every-claim
  precondition against the machine answer; "Claim identity is never carried by
  a scope." Round 1's F2 (a falsifier that was analytically empty flat and
  over-fired nested) is genuinely fixed: comparing the expanded value to the
  machine answer's value for that claim is well defined in every nesting, and
  nested override is now unreachable anyway, because a differing inner scope
  would falsify the outer scope's precondition. See F4 for the one residual.
- **Criterion 2 (Unknown).** No reading I could construct lets a scope value
  stand in for an Unknown claim: the precondition is over the machine answer,
  so a scope carrying a positive label ranges only over claims that are all
  positive there, and "absent after expansion" is a falsifier. "The machine
  answer SHALL carry every field on every claim and SHALL not inherit" is
  explicit. The one soft spot is F4, and it is an over-assertion by the scope,
  not a substitution for the claim.
- **Criterion 3 (oracles).** Both requirements keep an independent oracle that
  expands with "the checker's own statement" / "its own statement" of the rule
  and imports "no production vocabulary or rendering code"; PWB-REQ-007's
  independence bullet now also reads the machine answer, which is what makes
  its falsifier decidable. `scope-hidden` is named in the mutation proof as a
  distinct class beside missing/duplicated/changed/collapsed/wrong-evaluation,
  and "report both channel denominators for every run" survives unedited.
- **Criterion 4 (parity).** "a scope element contributes no tuple of its own
  after expansion" (007) and "contributes no marker of its own after
  expansion" (020) close round 1's F11; `collapsed` and `duplicated` are
  untouched in both the falsifier and the mutation list, and `design.md`
  decision 9 now names `scope-hidden` "beside its unchanged `collapsed` and
  `duplicated` falsifiers", which closes F5.
- **Criterion 5 (contract delta), partly.** Insert-only; applies identically to
  both mirrors and produces byte-identical results (verified, step 9); the
  non-citability sub-clause is excluded by name and stands unedited; the
  package says in four places that it binds only by a separate act
  (`SEMANTIC-DELTA.md` Artifact §, Migration step 3; `OWNER-DECISION-PACKET.md`
  :21-24, :144-149). F5, F7 and F8 sit against this criterion.
- **Criterion 6 (unchanged boundaries).** I checked the hunk headers against
  the requirement boundaries in the post-apply file: the three spec hunks land
  at 450 and 473 (inside PWB-REQ-007, 439–486) and 907–936 (inside
  PWB-REQ-020, 902–945). PWB-REQ-014 (759–815) and
  PWB-REQ-011/015/016/021/022 are byte-untouched. `spec.md`'s warrant blocks
  are unchanged and the regenerated dependencies verify, so "No warrant list
  changes" holds mechanically. RFC7-33 is already in PWB-REQ-007's
  `contracts:` list at `spec.md`:480 and in PWB-REQ-020's at :938, so no
  warrant needed adding. The delta's "does NOT change" list is accurate against
  the patches in every limb I could test — except that it asserts PWB-REQ-016
  unaffected without argument (F3).
- **Criterion 7 (package mechanics).** Manifest = post-apply bytes, 11/11
  (step 10). `--check` and `--selftest` fail closed on manifest drift, subject
  byte drift, path order, patch corruption, contract mirror drift and contract
  patch corruption (steps 4, 6). Cannot bind by merge: the manifest hashes
  bytes not in the tree, `--apply` refuses without `--at-adoption`, no script
  applies the contract patch at all, and `check_governance.py` is 0 FAIL at the
  reviewed commit with CG-7h still binding the 2026-09-05 package. The phrase
  is in `ACCEPTANCE-PHRASE-REGISTRY.yaml:44-49` and registered in
  `check_governance.py:1518-1523`; the existence-gated activation is at
  :2297-2313; the packet copy is caught by CG-7d/CG-7e (step 8, mutation
  verified). CI carries both builder steps
  (`governance-docs.yml:112-116`) and CG-26 reports 28 published / 28 hosted /
  28 shared.
- **Criterion 8 (comprehension).** See the restatement below; I could build it
  from the package alone.
- **Criterion 9 (owner packet).** One decision, three options, the
  recommendation marked; the phrase present at :133 and explicitly not offered
  at :136-140 with the reason and the consequence of replying anyway; "Silence,
  a partial answer, a commit or a merge performs nothing" at :124; "Nothing is
  implemented before both acts" at :162; inert banner at :3-6. Round 1's F19
  (the target-revision option missing) is closed as option (b). The only
  finding here is F6.

---

## Dispositions of round 1

The raw is `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-RAW.md` (verdict
REVISE, reviewed commit `9098b0b`), retained verbatim and named in
`SEMANTIC-DELTA.md` §Review. CC-REV-6 satisfied: all twenty are dispositioned,
none dropped, and the raw is preserved with a `-RAW.md` suffix.

| # | disposition claimed | holds? | the line that shows it |
|---|---|---|---|
| F1 | accepted — 014 no longer patched; RFC7-33 patch travels; two-act path | **yes** | `spec.md.patch` hunks are at 450/473/907 only; PWB-REQ-014 at `spec.md`:759-815 is byte-unchanged; `proposed/contract/…patch` exists and applies to both mirrors |
| F2 | accepted — falsifier compares expanded value to the machine answer | **yes** | `spec.md.patch:51-53`, "a claim's expanded value for any field differs from the value the machine answer carries for that claim" |
| F3 | accepted — one strict rule | **partly** | `spec.md.patch:15-18` states the strict precondition and the differ-case. But round 1's strict-branch resolution also said to keep the override sentence "only as the falsifier's condition-of-violation", and no falsifier over the scope was added — see **F4** above |
| F4 | accepted — "SHALL fail to render" removed | **yes** | `spec.md.patch:19-20`, "this holds for evaluation identity as for every other field, and nothing fails to render"; `grep -F 'fail to render'` over the patches returns only that line |
| F5 | accepted — decision 9 names `scope-hidden` | **yes** | `design.md.patch:28-30`, "PWB-REQ-020 gains the `scope-hidden` falsifier and mutant class … beside its unchanged `collapsed` and `duplicated` falsifiers" |
| F6 | accepted — P-68 is a register row | **yes** | `PENDING-OWNER-DECISIONS.md:194` (row) and :107 (the dated update note) |
| F7 | accepted — existence-gated activation added | **yes** | `check_governance.py:2297-2313`, `_activate_pwb_scoped_amendment_act_copy_registry()`, guarded on `os.path.isfile(PWB_SCOPED_AMENDMENT_ACT)` |
| F8 | accepted — builder in CI and the published battery | **yes** | `.github/workflows/governance-docs.yml:112-116`; `PROJECT-STATUS.md:252-253`; CG-26 reports 28/28/28 |
| F9 | moot — 014 not patched | **yes** | PWB-REQ-014's oracle-independence bullet is byte-unchanged |
| F10 | moot for the spec; the contract speaks of units, RFC7-33's own noun | **yes** | `contract/…patch:11-15` uses "unit" throughout and defers the rule to "the governing specification"; `spec.md.patch` uses "claim" throughout |
| F11 | accepted — scope contributes nothing after expansion | **yes** | `spec.md.patch:16-17` ("contributes no tuple of its own after expansion") and `:85-86` ("a scope element contributes no marker of its own after expansion") |
| F12 | accepted — `polaris-copy.ts` marked must; legend defines every value; "every other row" sentence replaced | **yes** | `IMPACT-LEDGER.md:80` (`**must**`) and :54-59 (the three-value legend); I checked the table's implementation column contains only `—`, `**must**` and `model` |
| F13 | accepted — figure stated at the baseline and at this draft's commit, additions enumerated | **no** | `IMPACT-LEDGER.md:24-35` states 87; both methods return 88, and the enumeration omits `PENDING-OWNER-DECISIONS.md` — see **F1** |
| F14 | accepted — figures dated to the evidence record | **yes** | `design.md.patch:12-14`, "as measured on 2026-09-13 (`docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`)" |
| F15 | accepted — header says the rows bind only by the act naming the digest | **yes** | `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt:2-3`, "These rows bind only by the owner act that names this file's digest … until that act is performed they bind nothing" |
| F16 | accepted — resolution wording taken | **yes** | `spec.md.patch:13-14`, "leaves the field absent, which the falsifier below forbids" — verbatim the round-1 resolution |
| F17 | moot (014 not patched); change class now enumerates every change | **yes** | `SEMANTIC-DELTA.md` §Change class: "The amended spec clauses admit a human rendering the current clauses forbid and add one falsifier class; the contract clause gains one permission paragraph … Nothing is newly forbidden; no falsifier is weakened." I could not find a patched change it omits |
| F18 | accepted — split | **yes** | `IMPACT-LEDGER.md:41` now says "six of the eleven manifest rows cite the identifiers; **separately**, three of the eleven rows change…" |
| F19 | accepted — option (b) | **yes** | `OWNER-DECISION-PACKET.md:115-119`, "(b) Revise the target and close lane B" |
| F20 | accepted — `--write` required, bare run refuses | **yes** | bare run exits 2 with "refusing: regenerating the manifest changes the act argument; pass --write" (step 6) |

Nineteen of twenty hold; F13 does not, and F3 holds only in part. The lesson
recorded under the table ("a spec change that invalidates an accepted clause
has to carry the contract delta from the first draft (CC-REV-2)") is the right
lesson and matches CC-REV-2's text, which I read at
`review-and-documentation.md`:52.

---

## What I could not verify

- **That 350 KB is achievable.** No measurement exists with scopes on any
  page, pre- or post-lane-A. The package says so; I am recording that I
  accepted the estimate as `[Inferred]` and checked only its arithmetic.
- **That the RFC-0007 successor ceremony is buildable in the no-signal shape.**
  I read the migration plan's description; I did not read
  `docs/POLARIS-NO-SIGNAL-AMENDMENT-TOOLING.md` or audit
  `check_governance.py`'s successor seam for how hard the RFC-0008/0009
  hard-coding is to generalize. The claim "no RFC-0007 amendment has ever been
  performed" I did not independently sweep.
- **Whether a scope-carried field survives an accessibility-tree trace.** This
  is F3's question; answering it needs a rendering that does not exist.
- **The three oracles' actual behavior.** I read the ledger's line references
  (`polaris-parity-sweep.test.ts:110`, `:415-423`;
  `polaris-epistemic-tuples.test.ts:83`, `:94`, `:231-233`) as claims about
  the baseline commit; I did not open the test files or run the suite, which
  is outside a governance-delta review's scope and would not change any
  finding.
- **The comparator sites' dispositions one by one.** I re-derived the citer
  *populations* by two methods (which is where F1 and F2 come from) and spot-
  checked classifications; I did not independently adjudicate all 80 rows of
  the PWB table or all 75 of the RFC7-33 table.
- **CG-7h's nine findings individually.** I confirmed the count matches the
  delta's claim; I did not read each predicate.

---

## Comprehension restatement

Written from the package alone, as criterion 8 asks.

**The rule.** Polaris today prints, on every single claim, that claim's whole
epistemic tuple — label, tier, one primary reason, any secondary reasons,
freshness, challenge state, and which evaluation produced it. When a hundred
claims sit in one table and all hundred say the same thing about, say,
freshness, the page pays for "freshness" a hundred times. The amendment says:
in the *human* page only, if a field's value is the same for every claim under
one enclosing element, you may state it once on that element instead of on each
claim. The element must carry a machine-readable marker saying it is a scope. A
claim that doesn't carry a field itself takes the value from the nearest
enclosing scope that does. A scope may carry a field **only** when every claim
under it has that value **in the machine answer** — not "mostly", not "by
default". If the claims disagree, the element carries nothing and each claim
carries its own value, and that includes the evaluation identity; nothing
refuses to render on that account. A scope never carries a claim's identity,
and after you expand it the scope itself contributes nothing — it is not an
extra claim. The machine answer is untouched: every field, on every claim,
always, no inheritance.

**The saving.** The Polaris page for the whole Butlers project has to fit under
a 2 MiB response ceiling — over it, the daemon serves a 503 and the reader gets
nothing. An earlier trim (lane A) got it from 2,132,656 to 1,478,637 bytes, so
the ceiling is safe, but the owner's working target of 1,400,000 is still
missed by about 79 KB, and pending Butlers repairs will add 418–443 KB more.
Stating shared fields once is estimated to save about 350 KB, which would land
the page near 1,130,000 — under the target with room for the repairs. That
number is an estimate carried over from a measurement of the *older*, bigger
page and has never been measured with scopes on anything.

**The risks.** Three. (1) Someone reading the page's raw HTML, or copying one
claim out of it, sees fewer fields than the machine form carries — the meaning
lives in the ancestor. The package's answer is that the rule is stated once in
the spec, restated in the page's own lede, and that the *oracles*, not the
reader, are the guarantee. (2) A rendering could hoist a value that is wrong
for one member; the new `scope-hidden` falsifier and mutant class exist to
catch exactly that, in both oracles, each of which must restate the expansion
rule in its own code rather than importing the renderer's. (3) Not stated by
the package, and my F3: a screen-reader user is in the same position as the
raw-HTML reader, and the requirement that governs that (PWB-REQ-016) is never
discussed.

**The two-act path.** The specification is not the only thing that forbids
this. The accepted contract clause RFC7-33 says every distinction is carried
"as a machine-readable attribute on the rendered unit" — so amending the spec
alone would leave the spec contradicting an accepted contract. Craft policy
CC-REV-2 says an invalidated accepted contract has to be updated in the same
logical change, which is why an RFC-0007 patch travels in this package. But a
contract change is an act escalation trigger, so it cannot ride along on the
behavior sign-off: the contract gets its own act first, then the behavior
manifest gets its own act, and only after both does an implementation bead
exist. The awkward part is that no RFC-0007 amendment has ever been performed
in this repository, and the existing successor machinery is hard-coded to
RFC-0008/0009, so the tooling has to be built before act one can even be
offered. Order matters and is stated: contract, then behavior, then code. If
the contract act happens and the behavior act is declined, nothing changes on
the page — the permission simply sits unused.

**The one owner choice.** Not "approve this". The single question is direction:
**(a)** proceed on the two-act path — build the ceremony, perform both acts,
then implement; **(b)** revise the 1,400,000 working target instead and close
lane B, since the page is already ~612 KB under the hard ceiling and the
pending repairs fit; or **(c)** decline outright and meet the remainder some
other way. The sign-off phrase for the behavior manifest is printed on the page
but explicitly **not offered** — no recorder exists that would accept it, and
the contract act has to come first. Silence, a merge, a commit or a general
"approved" performs nothing, and if nothing is said the 2026-09-05 PWB package
and RFC-0007 as accepted stay the authorities.

---

## Why REVISE

The repair is substantial and mostly good. All five of round 1's blocking
findings are genuinely addressed in the bytes: PWB-REQ-014 is out of the patch
set, an insert-only RFC7-33 delta travels with a two-act path, the inheritance
rule is strict and stated once, the falsifier now has a real referent in the
machine answer, the undisclosed "SHALL fail to render" prohibition is gone, and
`design.md` and the spec agree on which falsifier catches scope-hiding. The
mechanics are the strongest part: the manifest hashes exactly the post-apply
bytes 11/11, the builder's seven selftest fixtures all fail closed, the phrase
registration fires CG-7d and CG-7e on a mutated digest, the contract patch
produces byte-identical results on both mirrors, and nothing binds by merge.
Nineteen of twenty round-1 dispositions hold.

It is still REVISE, on three blocking findings.

**F1 and F2** are the same defect twice: the package's re-derived sweeps are
wrong at the commit it names — 88 not 87, and 77 not 75 — and one of them
carries a false universal about what the additions are. That matters more here
than a wrong number usually would, because F13 of round 1 was *this exact
finding*, the disposition says "accepted", and the repair reproduced the defect
in the repair itself. The ledger's entire function is to tell the owner, with a
denominator, what a pair of acts reaches; a ledger whose headline figures do not
survive a second method run this session is not yet doing that job. Both are
ten minutes' work to fix and re-derive.

**F3** is the one that needs new thinking rather than new arithmetic. This
amendment moves epistemic content off the unit and onto its container, and the
package never once mentions the requirement (PWB-REQ-016) or the contract
clause (RFC7-34) that govern whether content on a container is recoverable by a
reader who cannot see the page — while marking the accessibility renderer as
needing no change. RFC7-34 admits "structure" as a carrier and PWB-REQ-016's
own words say "by text", and which of those governs decides whether this
permission is lawful for a non-visual reader at all. The owner is being asked
to authorize a *contract* act partly on the strength of this impact analysis.
An analysis that never names the sibling clause its own subject is cited beside
six times in the same module is not complete enough to rule on.

None of the three touches the rule's substance. I expect a third round to be
short.
