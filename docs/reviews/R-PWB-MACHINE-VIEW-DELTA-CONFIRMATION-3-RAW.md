# Review — PWB machine-view amendment (round 4, third confirmation)
Reviewed commit: 194f8cd1e90877842786d7adae9df10893ed2495
Manifest SHA-256: 2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c
Verdict: CONFIRM WITH EXCEPTIONS

Manifest file's own SHA-256 (`PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`, sha256 of
the whole file's bytes): `2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c`
— identical to the act-argument digest above. For this package the act
subject (`PWB_MACHINE_VIEW_SUBJECT` in `scripts/check_governance.py:1544-1545`)
*is* the manifest file itself, so the two values coincide; they are not
always the same thing across packages (see AGENTS.md's "Say which digest the
raw's head must carry" lesson, added 2026-09-23) but they are here, and both
match the phrase `OWNER-DECISION-PACKET.md:172` quotes.

## Task 1 — Round-3 findings (F6–F9), re-derived

**F6 (revise) — sibling-count claim ("three" → "five" candidates carrying
`proposed/spec.md.patch` against the PWB `spec.md`).** Repaired and true at
this commit. I re-derived the population independently (not by reading the
prose): `find .syzygy/governance/contracts/candidates -name spec.md.patch`
plus a grep of each hit for the PWB spec path returns exactly five —
`pwb-machine-view-amendment`, `pwb-scoped-attributes-amendment`,
`pwb-exact-source-render-mode-scenario`, `pwb-opening-band-scenario`,
`pwb-missing-currency-disclosure-scenario`. All three cited locations name
the same five, with the same predicate ("carries a `proposed/spec.md.patch`
against the PWB `spec.md`") and the same commit (`76b4beb`):
`SEMANTIC-DELTA.md:549-551`, `OWNER-DECISION-PACKET.md:206-210`,
`IMPACT-LEDGER.md:117-122`. No new false count was introduced — the
sibling-composition sub-claims ("missing-currency before scoped-attributes
fails", "every order with scoped-attributes first composes to one digest")
are marked `[Observed]` and are consistent with `--check`'s own two-order
verification (see Task 2). **Discharged.**

**F7 (note) — round-2 disposition of F4 named a nonexistent heading.**
Repaired: `SEMANTIC-DELTA.md:658` (round-2 disposition body) now names
"Migration / supersession plan", and that heading exists verbatim at
`SEMANTIC-DELTA.md:510`. **Discharged.**

**F8 (note) — packet credited the recorder itself with registering the
successor-chain link.** Repaired: `OWNER-DECISION-PACKET.md:184-195` ("Two
acts, and why their order is free", item 2) now reads "…writes the
dedicated record and the aggregate section of `ACCEPTANCE-ACT-RECORD.md`;
**the same change** registers the chain link in `check_governance.py`" —
attribution moved off the recorder. I read
`scripts/record_pwb_behavior_amendment_acts.py:28-30` directly: "The
successor-chain link and the existence-gated copy registrations in
`check_governance.py` are the performing change's to add; this script
prints what it knows and edits no check." The repaired sentence matches the
docstring. **Discharged, with one residual, non-blocking, of the same
defect class** — see finding 1 below.

**F9 (note) — three ordering sections missing the owner's 2026-09-23
landing-order citation.** Repaired: all three name
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
§6 — `SEMANTIC-DELTA.md:566`, `OWNER-DECISION-PACKET.md:223`,
`IMPACT-LEDGER.md:134`. I confirmed the target file exists and its §6 is
literally "## 6. Landing order of the spec-touching packages" (grep of its
headings), so the citation is accurate, not just present. **Discharged.**

**New, non-blocking finding carried forward from the F7/F8 repair pass:**

1. **`SEMANTIC-DELTA.md:696-701` (the F8 disposition itself) names a
   heading, `"How this would be adopted" step 6`, that does not exist
   verbatim anywhere in the package.** I grepped every file in the package
   directory for the literal string `How this would be adopted`; the only
   hit is this disposition sentence itself. The content is correct — step 6
   of the real heading, `## Migration / supersession plan`
   (`SEMANTIC-DELTA.md:510`, item 6, "**At adoption, in the same logical
   change (CC-REV-2):**") does say `check_governance.py` gains the
   successor-chain link as part of the adoption change — but the disposition
   names the section by a paraphrase in quotes rather than its actual
   heading. This is the identical defect class F7 fixed one round ago (a
   disposition citing a section by a name the file doesn't carry). Non-
   blocking: content is truthful, only the anchor phrase is wrong. Repair:
   change `"How this would be adopted" step 6` to `"Migration /
   supersession plan" step 6`.

## Task 2 — machine checks (output read, not exit code)

`python3 scripts/build_pwb_machine_view_amendment.py --check`:
```
PWB machine-view amendment manifest matches 11 proposed behavior subjects (2 patched,
9 unchanged); the dependency declaration is regenerated from the proposed spec and the
spec patch composes with the sibling candidate in either order
```
Exit 0, and the printed sentence itself carries the denominator (11, 2, 9) —
matches `BEHAVIOR_SUBJECTS`/`PATCHED` in the script (`build_pwb_machine_view_amendment.py:68-95`).

`python3 scripts/build_pwb_machine_view_amendment.py --selftest`:
```
selftest: closed population, byte drift, path order, subject drift, context-line and
added-line patch corruption, transcribed and unwarranted dependency declarations,
sibling drift and a missing sibling patch fail closed
```
Exit 0. This message's predicate list is exactly criterion 9's list
(manifest drift, context-line and added-line patch corruption, a
transcribed declaration, a spec whose warrants stop validating [the
"unwarranted dependency declaration" fixture, `:357-362`], sibling drift,
missing sibling patch). I read the fixture code (`:275-383`), not just the
banner: each fixture mutates one input byte and asserts the specific
finding/failure fires, satisfying rule 6.

`python3 scripts/check_governance.py` (full battery): **0 FAIL**, 32 OK, 20
WARN (52 checks; WARNs are report-only/advisory by design, e.g. CG-1c/CG-8/
CG-27). Relevant lines: `CG-7d` (act digests quoted anywhere are current or
performed) shows the `SIGN OFF PWB MACHINE-VIEW AMENDMENT` phrase as one of
the 23-of-26 digest-bearing subjects with a quotation, 0 findings, "0
performed digest(s)" — correct, since no act has been performed.
`CG-7e` (act-argument copies enumerated and current) — 0 findings. No line
in the output names `pwb-machine-view-amendment` as a FAIL or as a stale
copy.

## Task 3 — digests

Act-argument / manifest-file digest, by script (`sha256sum`):
`2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c` — matches
`OWNER-DECISION-PACKET.md:31-32` ("Behavior manifest SHA-256") and
`OWNER-DECISION-PACKET.md:172` (the unoffered act phrase's argument), and
matches `PWB_MACHINE_VIEW_SUBJECT` in `check_governance.py:1544-1545`
(the manifest file path, not a row).

I also independently re-derived one manifest row without trusting the
builder: copied `spec.md` into a scratch tree, `git apply
proposed/spec.md.patch`, `sha256sum` the result —
`f57c37a8ae8fd287b9b3a807a6d641be327dbbffc13ec370de950bde2d23e2f8`, which
equals the `spec.md` row in `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` exactly.

## Task 4 — judgment against REVIEW-BRIEF.md and the CC-SPEC bar

1. **Change class.** The patch is pure insertion (`grep -c '^-'` on
   `proposed/spec.md.patch` = 1, and that one line is the diff header
   `--- a/...`, not a content deletion) — no existing PWB-REQ-020 sentence,
   bullet, Scenario or warrant is touched. Ground 3 of the Normative
   classification (SEMANTIC-DELTA.md, "The change class" section) is marked
   as the weakest and non-load-bearing per round-1's F2 repair, which I
   re-read and found still present. Holds.
2. **Closure.** Both categories are closed by enumeration ("A route enters
   either category only by a later amendment… naming it as a member");
   "neither admitted nor forbidden" is the same construction used
   elsewhere in this spec family and does not license an unnamed route
   affirmatively. Holds.
3. **Two genuinely-two categories.** The draft view's exclusion list
   ("no project-shape identity, statement, source anchor, coverage state,
   denominator or contradiction") is exhaustive against the exact field
   list PWB-REQ-020's own SHALL sentence names two paragraphs below the
   insertion (I diffed the two lists by hand: identity, statement, source
   anchor, coverage state, denominator, contradiction, body-read-authority
   state, walkthrough-judgment state/disclosure — the draft view's excluded
   set is a subset naming the first six, and it carries none of the other
   two either since it "mints no project fact" and "composes only… one
   generation run"). Holds.
4. **Parity not weakened.** Confirmed above by the zero-deletion patch
   fact; PWB-REQ-020's Case/Observable/Oracle/etc. text sits unchanged
   further down the same file, outside the patch's hunk. Holds.
5. **RFC6-21.** Both quoted sources check out byte-for-byte against the
   tree: `RFC-0006…md:524-526` (item 7 of "Violation cases") and
   `contract-coverage-matrix/RFC-0004-0006.md:234` (the `RFC6-21.c2` row) —
   both quotes in `SEMANTIC-DELTA.md` match verbatim. On substance, I read
   `RFC-0006` §3.x's actual RFC6-21 clause (line 382-385): "…endpoints
   always serve the full set." Literally, this reads more naturally as a
   property of every endpoint than as "at least one endpoint remains
   complete," which is the delta's narrow gloss — so the tension the delta
   flags is real, not manufactured. I do not find the wide reading
   compellingly *forced*, though: RFC6-21's stated purpose (per its own
   sentence) is guarding against "minimal" becoming "a fourth epistemic
   state" by silent, permanent subtraction — SDR-17's minimal-*display*
   concern — and a closed, declared, byte-ceilinged view that coexists with
   an unmodified complete machine answer at the same evaluation does not
   create that silent state. Consistent with all three prior rounds, I do
   not treat this as forcing a REVISE; the disclosure is honest, sources
   are quoted exactly, and the delta itself states plainly what changes if
   a reviewer decides otherwise ("that is a finding, not a question").
   Non-blocking, disclosed-not-resolved, as recorded.
6. **Ceiling precondition.** "A member served under a byte ceiling of its
   own SHALL NOT be served before the adapter-registry entry's resource
   envelope declares that ceiling" names no field. `IMPACT-LEDGER.md`'s
   grep for the field ("No registry file names it") is consistent with what
   I found: no `.toml`/registry file under the repo declares this ceiling
   field today, so there is no dangling literal, and the sentence
   constrains only the two named members, not the existing
   `/api/poc/polaris` member (whose ceiling the registry already declares,
   per item 3 of "What explicitly does NOT change"). Holds.
7. **Unchanged boundaries.** Eleven items enumerated
   (`SEMANTIC-DELTA.md:290-341`), tested against the patches: item 2's
   "byte-identical" claim is the same zero-deletion fact from criterion 1;
   item 9's regeneration claim I re-ran myself this session —
   `python3 scripts/build_polaris_project_wide_contract_coverage.py --check`
   → "Polaris consequence matrix matches regeneration — 324 clauses
   represented" (rule 7: valid for this commit, re-run this session, not
   copied from an earlier round). Holds.
8. **Blast radius.** Re-derived independently, not read: at baseline
   `a4a34510a5582edbd38c1df57a064ba3ac0a33f2`, tracked-file count (`git
   ls-tree -r -z --name-only`) = **1,334**; a Python `re` sweep of every
   file's UTF-8 text for `PWB-REQ-020\b` = **112** files (method 1's full
   form), matching a second method (`grep -rl -F PWB-REQ-020` over a `git
   archive` extraction of the same commit) = **112**. The continuation
   pattern the ledger states
   (`PWB-REQ-\d{3}(?:\s*[/,]\s*(?:and\s+)?\d{3})*\s*[/,]\s*(?:and\s+)?020\b`
   plus a `..` range form) adds exactly the same **9** files the ledger
   names, confirmed by printing each match. Total **121 / 1,334**, exact
   match to the ledger's claim, with the same 9-file list. Holds, per rule 2
   (re-run this session) and rule 9 (denominator stated and covers the
   forms the identifier occurs in).
9. **Package mechanics.** Covered by Task 2. `--check` fails closed on
   drift and enforces the declared patched-subject population; `--selftest`
   exercises every listed failure mode with real mutated fixtures, not
   banner claims. The candidate directory carries the "binds nothing"
   banner (`IMPACT-LEDGER.md:3-6`, `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt:2-3`)
   and nothing in `openspec/` differs from the last performed act on this
   commit (the two subject rows that differ are *proposed*-bytes rows, not
   tree bytes — `--check` says "2 patched" meaning 2 of 11 rows differ from
   current tree bytes, which is what "candidate, inert" requires). Holds.
10. **Sibling ordering.** Covered above (F6) and by `--check`'s own
    "composes with the sibling candidate in either order" line, which I
    take as scripted rather than asserted since `coexistence_findings()`
    (`build_pwb_machine_view_amendment.py:186-217`) actually applies both
    patch orders in a scratch tree and diffs the bytes. Holds.
11. **Comprehension.** As a reader with no authoring context I can restate:
    two closed categories exist — "derived read-only machine view"
    (Polaris presentation + `/api/poc/polaris` + a new `/api/poc/briefing`,
    all machine-credentialed, all derivable from the machine answer, all
    byte-ceilinged) and "generated editorial draft view" (one member,
    `GET /polaris/draft/<runId>`, carrying no project-shape fact at all);
    the owner is asked whether this drafted realization matches P-72/P-76,
    with (a)/(b)/(c) arms; adoption authorizes no route, no registry edit,
    and no implementation — a separate bead does that. This restates
    cleanly without needing the author's context, satisfying criterion 11.
12. **Owner packet.** The sign-off phrase is present and explicitly stated
    as **not offered**, with a truthful, rule-10-shaped reason
    ("the two fresh-context rounds confirm the commits they reviewed, not
    these repaired bytes… the behavior recorder… carries no entry for this
    package yet" — I confirmed `record_pwb_behavior_amendment_acts.py` has
    no `pwb-machine-view` entry). The quoted digest equals the file the
    builder writes (Task 3). "Silence, a partial answer, a commit or a
    merge performs nothing" is stated plainly
    (`OWNER-DECISION-PACKET.md:161-163`). Nothing in the packet authorizes
    an implementation, route or registry edit (item 7 of the migration
    plan, and the packet's own banner). One defect found here:
    **`OWNER-DECISION-PACKET.md:148` says "Two rounds have run as of
    2026-09-23, see the date line"**, but the same document's own opening
    paragraph (`OWNER-DECISION-PACKET.md:8-11`) says **three** rounds have
    run (round 1, round 2 at `9d74185`, round 3 at `76b4beb`), and the
    "date line" the sentence points to is that same three-round paragraph.
    This is the same defect class as F6 (a round-count that went stale on
    a later landing and was not updated everywhere) — here it is the count
    of *review* rounds rather than *sibling* candidates, and it sits
    directly under criterion 12 (owner packet accuracy). It is non-
    blocking (it does not change the sign-off phrase, the digest, or the
    "not offered" conclusion — both "two" and "three" support the same
    not-offered reasoning), but it is a false current-state sentence in
    the one document the owner reads to decide, so I judge it worth
    naming as its own finding rather than folding it into F6's closed
    disposition.

## Findings summary

1. **(non-blocking)** `SEMANTIC-DELTA.md:700-701` — the F8 disposition
   names a section, `"How this would be adopted" step 6`, that is not a
   heading anywhere in the package (only `## Migration / supersession
   plan` exists, at `SEMANTIC-DELTA.md:510`, whose item 6 is the section
   meant). Repair: rename the citation to `"Migration / supersession plan"
   step 6`.
2. **(non-blocking)** `OWNER-DECISION-PACKET.md:148` — "Two rounds have
   run as of 2026-09-23" contradicts the same file's own header
   (`OWNER-DECISION-PACKET.md:8-11`), which correctly states three rounds
   have run as of this commit. Repair: update to "Three rounds have run…"
   (or generalize the sentence the way F6's repair generalized the
   sibling count, so a fourth round does not require another point edit).

No blocking findings. F6, F7, F8 and F9 are each repaired truthfully at
this commit, with no new false claim introduced by any of the four
repairs — the two residual issues above are pre-existing staleness in
adjacent prose that the F6–F9 repair pass did not reach, not regressions
caused by it. `--check`, `--selftest` and the full `check_governance.py`
battery are green (0 FAIL) at this commit, independently re-run this
session. The blast-radius figure (121/1,334) and the sibling-patch count
(5) both re-derive exactly as claimed, by two independent methods each.
The act-argument digest and the manifest file's own digest are identical
(`2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c`) and
match the packet's quoted, not-yet-offered phrase.

## Method and commands

- `git rev-parse HEAD`, `git status --short` — confirmed clean tree at
  `194f8cd1e90877842786d7adae9df10893ed2495`.
- Read `REVIEW-BRIEF.md`, `SEMANTIC-DELTA.md` (all sections, in full),
  `OWNER-DECISION-PACKET.md` (in full), `IMPACT-LEDGER.md` (Discovery
  method, population, and Ordering sections), `PWB-BEHAVIOR-AMENDMENT-
  MANIFEST.txt`, `proposed/spec.md.patch`, `proposed/GOVERNING-
  DEPENDENCIES.md.patch`, `scripts/build_pwb_machine_view_amendment.py`
  (in full), `scripts/record_pwb_behavior_amendment_acts.py` (docstring
  and header), `scripts/check_governance.py` (the `PWB_MACHINE_VIEW_*`
  constants and their use sites).
- `python3 scripts/build_pwb_machine_view_amendment.py --check`
- `python3 scripts/build_pwb_machine_view_amendment.py --selftest`
- `python3 scripts/check_governance.py` (full battery; read the printed
  lines, grepped for `machine-view` and for `^FAIL`)
- `python3 scripts/build_polaris_project_wide_contract_coverage.py --check`
  (re-ran the coverage regeneration claim myself, this session)
- `sha256sum` on `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` directly.
- Independent manifest-row re-derivation: copied `spec.md` into a scratch
  `git init` tree, `git apply --whitespace=nowarn proposed/spec.md.patch`,
  `sha256sum` the result, compared to the manifest's `spec.md` row byte for
  byte.
- Sibling-count re-derivation: `find .syzygy/governance/contracts/
  candidates -name spec.md.patch`, then grepped each for the PWB spec path
  to exclude any patch not targeting this spec (none excluded; 5 remain).
- Blast-radius re-derivation: `git ls-tree -r -z --name-only
  a4a34510a5582edbd38c1df57a064ba3ac0a33f2` for the denominator; a Python
  `re` script applying the ledger's own stated full-form and continuation
  regexes over every tracked file's decoded text at that commit (`git show
  <commit>:<path>`); cross-checked the full-form count with `git archive
  <commit> | tar -x` into a scratch dir and `grep -rl -F PWB-REQ-020`.
- Quote verification: `sed -n` over the exact line ranges
  `SEMANTIC-DELTA.md` cites in `RFC-0006-cross-surface-selection-query-
  drawer.md` and `contract-coverage-matrix/RFC-0004-0006.md`, diffed by
  eye against the quoted blocks.
- Grepped the whole package directory for `How this would be adopted` (one
  hit, the disposition itself) and for `Two rounds`/`Three rounds` (one
  hit each, in tension).
- Did not open `.syzygy/local/`, did not read any commit message body
  (subject lines only), did not consult other agents, and made no edits.
