# Launch-gate instrument — v2.2 → v2.3 semantic delta

> **A delta, not an approval.** The instrument remains a **candidate**; its
> approval as process policy is **P-34**, ungranted.
>
> **Nothing here is confirmed.** v2.3 repairs two `REVISE` verdicts, made by
> the session that received them. A repair session cannot confirm its own
> repairs — a sentence this file family has now written three times, about
> three successive versions. What is different this time is stated at the
> end: the changed bytes were put back under review in the same round.
>
> The v2.2 delta is **not superseded and must not be edited**: RD-55 and
> RD-56's repairs are accounted there, and RD-61/RD-62 verified that
> account against the bytes (all ten RD-55 findings closed; RD-56's
> substance closed with two disclosed-open residues). This file accounts
> only for what v2.3 changes.

## Why there is a v2.3

v2.2's two commissioned reviews — the first fresh-context reviews of any
repaired launch-gate bytes — both returned `REVISE`:

| Review | Subject | Verdict | Findings |
|---|---|---|---|
| RD-61 | policy semantics | `REVISE` | 1 blocking, 5 material, 5 minor |
| RD-62 | schema, validator, renderer | `REVISE` | 1 blocking, 6 material, 6 minor |

Dispatched concurrently, in fresh context, against frozen commit `918574c`,
neither seeing the other. **They independently found the same defect
again** — RD-61 f1 and RD-62 f5 are one hole: the "committed schema" was a
committed *path*, and the bytes at that path were read from the working
tree. The prior round's convergence (RD-55 f1 / RD-56 f1) repeated at the
next layer down.

Both reviews also confirmed the v2.2 repairs they were commissioned to
check: RD-61's differential battery found **nothing weakened** across
v2.1 → v2.2, reproduced the RD-55/RD-56 blocking attack and watched it
fail at all four surfaces, and swept 814 free-text injection sites with
zero leaks. The new findings are in the v2.2 additions themselves and in
ground the prior reviews had not walked.

## The blocking repair — the committed schema is bytes

`validate()` now resolves the schema from **`git show HEAD:`** and treats a
drifted working-tree copy as an `LA-1` error of its own; validation runs
against the committed bytes either way. `--schema` keeps its inspection
error; with git unavailable the filesystem fallback is already ineligible
through the fifth eligibility limb. The attack RD-61 built — an in-place,
audit-clean enum widening admitting `"Met (with caveats)"` into an
eligible `READY FOR …` record — is a fixture now, asserted in both
directions: the committed bytes reject the word, and the drift itself
errors.

## Every other repair

| Finding | Repair |
|---|---|
| RD-61 f2 — off-branch `repository_commit` | the named commit must be an ancestor of `HEAD` (`LA-2`); §2 states the rule; fixture uses a real dangling commit built with `commit-tree` |
| RD-61 f3 / RD-62 f9 — `SDR-n` resolved from a log; "one list, both branches" false | `_sdr_exists` greps only `SURFACE-DECISION-RECORD.md` for the `**SDR-n**` definition shape; §5 states the owning-record rule; the stale comment is rewritten |
| RD-61 f4 — whitespace `routing_authority` switches `LA-3b` off | an empty-after-normalization value is its own `LA-3b` error; the fixture's expectation names the *empty* wording, and its mutation test caught the bare-`LA-3b` expectation passing for the wrong reason |
| RD-61 f5 — §2 obliged a trend-row disclosure the generator cannot emit | the obligation moved to the record and the **generated report** (which prints `Model family`); §4's F5/F6 parenthetical moved with it. This is a semantic correction of an unmeetable obligation, argued in place in §2 |
| RD-61 f6 / RD-62 f2 — `--prior` reads outside the repository | the CLI flag gets the same containment as the record path (`LA-15`) |
| RD-62 f3 — the prior file need not be the declared identity | the loaded file's own `repository_commit` must equal `prior_record.repository_commit` (`LA-15`), on both paths |
| RD-62 f4 — an escaping declared prior collapsed to "declares no prior" | it computes `Unknown`, never absence — the RD-47 f3 rule, applied to its own repair |
| RD-62 f1 — `\r` defeats `_cell`/`_quoted` | one vertical-whitespace class (`\r\n\v\f\x85  `) at every neutralizer; `_quoted` splits with `splitlines()`; three `\r`-spelled forgery fixtures, verified to fail with the repair reverted |
| RD-62 f6 — "record valid", exit 0, git unavailable | the CLI prints "NOT fully validated … diagnostic only" and exits 2; the renderer exits 2 after writing its UNVERIFIED-stamped report |
| RD-62 f13 — `--check` misreads a git-less mismatch as an edit | that state renders `Unknown(git unavailable)` with its own exit status |
| RD-62 f11 — `$` matched before a trailing newline | patterns match with `fullmatch`; the audit refuses an unanchored pattern, so the two semantics cannot diverge silently |
| RD-62 f12 — invisible-character strip was an enumeration | stripped by Unicode category (`Cf`/`Cc`, tab/newline/CR excepted) |
| RD-62 f10 — `counterexample` and `falsification_summary` unchecked for substance | both run the placeholder lexicon (`LA-6`, `LA-14`) |
| RD-62 f7 — five live predicates had no discriminating fixture | fixtures added for the `fresh_context` eligibility limb, `_is_ancestor` (against a commit that *exists*), `--prior` commit equality, and the E4 case-index run; the two dead branches RD-62 verified are handled below |
| RD-62 f8 — a green fixture named a property it does not test | renamed to what it tests (`a wave set differing from §8's`), with the unreadable branch's coverage noted beside it |
| RD-61 m1 — "not rendered at all" false of `--allow-invalid` | §5 scoped to the default invocation and names the stamp |
| RD-61 m2 — "a function of the rows and nothing else" false of E3/F2 | §4 scoped to the record's own content |
| RD-61 m3 — the fourth outcome respelled per surface, limbs named nowhere | `gate_result` is the one string `NONE — <limbs>`; every surface prints it; the unreachable literal `NO FORMAL GATE RESULT` is gone |
| RD-61 m4 — the v2.1 changelog's unscoped absence claim | annotated in place with the scoped form |
| RD-61 m5 / RD-62 f7 — two LA-12 guard branches unreachable by construction | removed, with the construction argument in place: `plain` requires `n_deferred == 0`, `deferrals` requires an F2 deferral. Both reviews verified the unreachability independently. §4's "any other owner deferral" prose is aligned with the formula's exactly-one-substitution rule |

## What did not change

The **schema** is byte-identical (its unchanged full digest is in the
table below) — RD-56 f11's
deliberately-open `question_digest` alternative stays open for exactly the
reason recorded there: closing it moves the digest the formal packet
seals. The roster, the question texts, §8's parameter block, the verdict
vocabulary, and the §4 formula's conjuncts are untouched; every §4/§5
change above is a scoping or a strengthening argued beside its clause, and
the readiness meaning of every verdict word is unchanged. The §6 trend
table keeps its nine columns.

## Disclosed limits carried forward

RD-56 f11 (`question_digest` sha256 form binds nothing — schema-frozen);
RD-56 f13 second half (`counterexample: " "`) is now closed by the
placeholder check; RD-62 f9's residual (a warrantable file added to the
decisions home tomorrow joins the path branch's classification, not a
list) is narrowed by the identifier branch's owning-record scope.

## Fixtures

`--selftest`: validator 101 → **119**, renderer 31 → **34**. Six repairs
were mutation-tested by hand in this pass — each reverted on a copy and
its fixture watched to fail: the `fresh_context` limb, the schema byte
identity, ancestry, `fullmatch`, the LA-3b guard (which caught its own
fixture's first expectation passing for the wrong reason), and `--prior`
containment, plus the two `\r` forgery sites against the reverted
neutralizers.

## Digests at this delta

```text
launch-gate-pre-specifications.md          3e65aaa39bd6525c70ce589fb3f0c029af91b1bb74b29966563d3f3dcf376294
launch-gate-administration.schema.json     e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb  (unchanged)
scripts/validate_launch_administration.py  c3e20de8304430ff94ad68f65b1ec62695779a632b09fff8a64d1be94f40e52c
scripts/render_launch_administration.py    678dab0a232958116993c6736af9f3b2d72120db8de93e6880aa480e9df13ceb
```

The formal launch packet seals digests that this delta moves; the packet
is **stale against v2.3** and is re-sealed only after the v2.3 reviews
return, not before — sealing unreviewed bytes is how its stop rule fired
last round.

## What must happen next

One fresh policy-semantics review and one fresh machinery review of the
**v2.3 bytes** (the RD-55/RD-56 commission, third administration). If both
confirm: freeze v2.3, update the P-34 packet, re-seal the formal packet.
If either finds a real false-READY path: repair that bounded issue,
re-review the changed bytes. This round dispatches them itself rather than
leaving the gap the round-08g pass left.
