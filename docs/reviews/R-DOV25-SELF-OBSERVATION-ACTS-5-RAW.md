# R-DOV25-5 — confirmation review of PR #120
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 1a5c03aac4a6c06ccabb538b0884c2972a0b46c0
Manifest rows (act arguments, proposed-bytes sha256): consent 2901eccbc92cfcec8aaae0ec5817dd70a74d333bb3af321c81e094fc47c022e4; registry 6b3d0b9992cc4c1e6217013a62c3fc6d32e3077559895553f5234e287c423fce; policy 4155733ddad27abe471131baae98c681da2731d79851339a08ff5914700faf32

- Subject: `origin/agent/tier4-dov25` at `1a5c03a`, two commits on top of the round-4 reviewed commit `a20c263` (`b2407b2` builder and prose repair, `1a5c03a` partition recount).
- Package: `.syzygy/governance/contracts/candidates/pwb-self-observation-acts/` and `scripts/build_pwb_self_observation_acts.py`.
- Reviewer: fresh-context agent, read-only, detached worktree. Nothing on the branch or in the main checkout was edited, committed or pushed. All draft, patch and builder mutants ran in `git archive` exports of `1a5c03a` in the scratchpad, never in the worktree (`git status --short` clean afterwards).
- Head: follows the brief's "The raw's head" predicate. Line 4 carries the three manifest *rows* (proposed-bytes digests), not the digests of the manifest files.
- Date: 2026-09-27.

## Commands run and outputs read

| Command | Output read |
|---|---|
| `python3 scripts/check_governance.py` | `32 OK, 20 WARN, 0 FAIL (52 checks)` |
| `python3 scripts/check_governance.py --selftest` | `285 fixtures, 0 failing` |
| builder `--check` | exit 0. "3 manifests match their 3 proposed artifacts". consent `2901eccb…`, registry `6b3d0b99…`, policy `4155733d…`, all `(pending)` |
| builder `--selftest` | exit 0, `selftest: 190 predicates` |
| builder `--diff` | prints the proposed patch: two hunks, version line `1.1.0-candidate.1` → `1.2.0-candidate.1`, and the `selfObservationScope` block inserted before `governingBehaviorContract` |
| `scripts/check_docs_review_campaign_partition.py` | `total=252 assigned=252 raw=227 other=25 unmatched=0 overlaps=0`; row "P-74 Q3 self-observation acts gate" count 4 |
| `cmp` of the scratchpad round-4 raw with `docs/reviews/R-DOV25-SELF-OBSERVATION-ACTS-4-RAW.md` | identical (CC-REV-6) |
| `git diff a20c263 HEAD --stat` | 6 files: packet, brief, delta, `docs/README.md`, the retained round-4 raw, the builder. Nothing under `proposed/` and no manifest changed [Observed] |
| Rule 3, independent digests | `sha256sum` of the two drafts gives consent `2901eccbc92c…22e4` and registry `6b3d0b9992cc…3fce`. For the policy, I extracted it with `git archive`, applied the proposed patch with `patch -p1`, then ran `sha256sum` (`4155733ddad2…faf32`) and `json.load` (valid). All three equal the manifest rows, the `--check` output and, for acts 1 and 2, the packet's quoted arguments (`OWNER-DECISION-PACKET.md:66, 82`) [Observed] |
| n9 figures | `git ls-tree -r -z --name-only` count: 1,561 at `64746a4`, 1,562 at `a20c263`, 1,563 at `1a5c03a`. `git grep -F -n '1.1.0-candidate.1' <c> -- apps packages scripts`: 22 lines at all three commits, 3 of them in the builder. The ledger's population is 348 files under `apps/`, `packages/` and `scripts/` at all three commits [Observed] |

## Round-4 resolution (S1, n7–n9)

| Finding | Severity | Resolved? | Evidence |
|---|---|---|---|
| S1 — `--check` claim wider than the check; widened drafts regenerate and pass | revise | **Resolved** | [Observed] `consent_findings` (`scripts/build_pwb_self_observation_acts.py:834-836`) compares the whole draft with `CONSENT_TEXT` byte for byte. `registry_findings` (`:811-814`) compares the whole draft with `REGISTRY_TEXT`, which takes only the spec digest from the tree. `policy_findings`/`policy_expected` (`:756-790`) compare the patched policy with the base plus exactly the version line and the rendered `SELF_SCOPE`. All 18 round-4 survivors (C14–C19, C21, R12–R21, R23) are selftest cases (`:1111-1133`, `:1273-1312`). I re-ran my own versions of C14, C16, C17, C18, C21, R12, R13, R16, R17 and R23 against `--check` in an export: every one was killed, both plainly and end to end. The round-4 end-to-end route (R12 + C17, `--write`, refresh both packet digests, `--check`) now exits 1 with exactly the two draft findings. The claim sentences (`OWNER-DECISION-PACKET.md:328-338`, builder docstring `:20-29`, comment `:120-124`) hold for every draft and patch-output mutation I tried (below). The exceptions are in the notes, all outside the drafts and the patch output: the policy base, an installed policy, and the patch file's own bytes |
| n7 — key-order predicate had no mutant | note | **Resolved** | [Observed] The key-order predicate is replaced by the byte comparison. The selftest case "registry entry keys reordered" is present (`:1313`). My own swap of the entry's key order, keeping every key and value, fails `--check` from line 9 |
| n8 — docs README misnamed the column | note | **Resolved** | [Observed] `docs/README.md:97` now reads "R1 two sentences still presenting the P-74 "What it means" column as the ruling". The new round-4 cite `R-DOV25-SELF-OBSERVATION-ACTS-4-RAW.md:2` points at the line `Verdict: REVISE` |
| n9 — 1,561 was the pre-repair population | note | **Resolved** | [Observed] `OWNER-DECISION-PACKET.md:430-435` carries a dated correction: 1,561 at `64746a4`, 1,562 at `a20c263`, and 22 lines over 348 files. All three re-derive (table above) |

## Rule 6 — mutants

**Drafts and patch output against `--check`.** Each case ran in a fresh `git archive` export of `1a5c03a`, in two modes. The plain mode edits and runs `--check`. The end-to-end mode edits, runs `--write`, replaces both quoted digests in the packet with the new manifest rows, then runs `--check`.

- Consent: 13 cases, all killed in both modes.
  - Byte-only changes: one flipped byte, a trailing space, an extra final newline, a dropped final newline, CRLF line endings, a BOM, an appended NFD character.
  - Widenings: C14, C16, C17, C18, C21.
  - An invalid UTF-8 byte is also killed, but by an uncaught `UnicodeDecodeError` traceback (exit 1) rather than a finding.
- Registry: 11 cases, all killed in both modes.
  - Byte-only changes: re-serialized at indent 4, compact re-serialization, one `e` escape, entry keys reversed, a trailing space.
  - Widenings: R12, R13, R16, R17, R23.
  - A spec digest of zeros.
- Patch output: 7 cases, each a regenerated patch whose output differs from the current output. All killed in both modes.
  - One byte changed in the self scope.
  - A trailing space.
  - One base (Butlers) value changed through the patch.
  - The self-scope keys reordered.
  - `cache` added to `ingestBoundaries`.
  - A `o` escape.
  - A dropped final newline.
- Control: a patch regenerated to yield the same output passes in both modes, as the packet says (`:336-338`).

**Other routes to a changed policy.** None of these is a draft or patch-output change. See n12 and n13.

- (1) Pre-adoption, a Butlers value changed in the *base* policy, then `--write`, then `--check`: exit 0. `check_governance.py` fails CG-7e, with 6 findings naming the performed policy act's argument copies.
- (2) After `--apply policy --at-adoption`, a Butlers value changed in the *installed* policy, then `--write`, then `--check`: exit 0.
- (3) A `/dev/null` → `apps/evil.txt` creation hunk appended to the patch file: `--check` exits 0, and `--diff` prints the hunk. After `--apply policy --at-adoption`, `--check` fails: "…patch does not apply on the current bytes…".
- (4) A line of prose prepended to the patch file: `--check` exits 0.

**Builder against `--selftest`.** 18 mutants, each applied to a copy of the builder in an export.

- Killed (15):
  - the drafter's ten: consent, registry and policy comparisons off; `text_findings` equality weakened to length equality; stale diagnosis off; anchor check off; seed check off; spec token not substituted; no-op check off; Butlers collision off;
  - exact-regeneration check off;
  - packet stale-digest comparison off;
  - `policy_expected` without the scope;
  - `policy_expected` without the version bump;
  - installed-target byte comparison forced `True`.
- Survived (3):
  - B11: the end-to-end case's consent widening made a no-op.
  - B17: the end-to-end case's registry widening made a no-op.
  - B12: `pol()` ignoring its mutation.
  - See n10 and n11.

## Attribution and VIS-4 sweeps

- [Observed] Owner attribution. The sweep ran Python `re`, case-insensitive, `\b(ruling|rulings|ruled|chose|chosen|decided|answer|answers|answered|you|your)\b`, over the 11 tracked files of the package and the builder. It returned 70 lines, all read.
  - The round-4 repair adds no owner-attributed sentence. The only new "you/your" line in the diff is the unchanged "only your act makes an act performed" (`OWNER-DECISION-PACKET.md:358`).
  - The quotations re-checked against the decision records are byte-exact:
    - the P-74 Q3 Ruled cell, "three acts scoped to a test-only self-observation (consent record, second registry entry, secret-policy extension) before slice 6 runs" (`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:64`);
    - "took the recommended option on each with no edits" (same file, `:10-11`, wrapped);
    - "Retire it in the adoption change (Recommended)" (`POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md:75`);
    - "Readiness order, lane B last (Recommended)" (`POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:114`);
    - the "What it means" sentence, still attributed to the record's reading (`OWNER-DECISION-PACKET.md:281-283`).
  - The builder's `CONSENT_TEXT` is byte-identical to the unchanged consent draft, so it adds no new attribution.
- [Observed] VIS-4. The sweep ran `\b(adopted|accepted|approved|in force|performed|installed)\b`, case-insensitive, over the same 11 files and returned 68 lines. The lines in the diff since `a20c263` were read in full. The repair makes no adoption, acceptance or approval claim. "Installed" stays defined as bytes in place (`OWNER-DECISION-PACKET.md:357-358`).

## New findings

### n10 — note — the end-to-end selftest case is weaker than its disposition says

The round-4 S1 disposition (`OWNER-DECISION-PACKET.md:479`) says `--check` "must then fail with only the two draft findings". The predicate at `scripts/build_pwb_self_observation_acts.py:1563` is `if not got or any("draft" not in f for f in got)`. It accepts a single draft finding.

[Observed] B11 (the consent widening made a no-op) and B17 (the registry widening made a no-op) each survive `--selftest` at 190. [Observed] The real end-to-end run does yield exactly the two draft findings, so the `--check` guarantee is unaffected.

This is a test-rigor gap in a disposition's description, and the same class as round-4 n7. Fix: require `len(got) == 2` and one finding each naming the consent and registry drafts, or say "at least one draft finding and nothing else".

### n11 — note — the policy value mutants are vacuous

`pol()` at `scripts/build_pwb_self_observation_acts.py:1395-1398` returns `json.dumps(doc, indent=2).encode()` with no final newline, but the patched policy ends in one. Every `pol()`/`self_scope()` mutant therefore differs from the expected bytes at the last byte, whatever it mutates.

[Observed] B12 (`pol()` ignoring its `fn`) survives `--selftest` at 190. The byte comparison is the one policy predicate, so no current check goes unexercised: the three byte-only cases at `:1462-1476` kill a disabled comparison on their own. But the ~26 value mutants prove nothing beyond "a missing final newline fails". A mutant that silently became a no-op would still score as killed.

Fix: append `+ b"\n"` in `pol()`, as `reg()` already does at `:1150-1153`, and assert each mutant differs from `proposed` somewhere other than its end.

### n12 — note — the unpinned patch file can carry content `--diff` shows and the act never binds

The packet says the patch file's own bytes are not compared (`OWNER-DECISION-PACKET.md:336-338`). It also says `--diff` "prints the policy change in full" (`:359-360`), and `main()` prints the patch file verbatim (`scripts/build_pwb_self_observation_acts.py:1694`).

[Observed] A prepended prose line, or an extra hunk creating `apps/evil.txt`, passes `--check`. `--diff` then shows it to the owner as part of "the policy change". With the extra creation hunk, `--check` fails once `--apply policy --at-adoption` has run, because the reverse no longer applies. That contradicts "`--check` passes before, between and after the three adoptions" (`:157`) for a patch that passed pre-adoption.

The current patch has neither. The act argument is the policy digest, so nothing extra would bind [Inferred]. The declared unpinned item is accurate as stated.

Fix: require the patch's only `---`/`+++` target to be the policy, with nothing before the first header, or have `--diff` print a diff regenerated from base → expected rather than the file.

### n13 — note — "any byte change to what the patch produces" is relative to the base policy

The `--check` bullet at `OWNER-DECISION-PACKET.md:331-335` and the docstring at `:22-26` define the policy comparison against "the base policy's bytes". They then say "any byte change … to what the patch produces, fails `--check`". [Observed] Two routes change the produced bytes and pass the builder's `--check` after `--write`:

- Pre-adoption, a change to the base policy (route 1). This is a change to a performed act's argument, and `check_governance.py`, the fourth command in the same "How to verify" block, fails it under CG-7e.
- Post-adoption, a change to the installed policy outside the self scope (route 2). The builder reverse-derives the base, so it cannot see the change. A new-file target changed after installation *is* caught (`target_state`, `:849-860`). The installed policy would rely on act 3's own digest record [Inferred; no act record exists yet to test].

Neither route edits a draft or the patch output, so I read the sentence, in its base-relative context, as true. Adding "relative to the current base; the base itself is guarded by the act in force (CG-7e)" would make it self-contained.

## Verdict

S1 and the notes n7–n9 are repaired as their dispositions say. Both drafts are now pinned whole, and the policy output is pinned relative to its base.

- 31 draft and patch-output mutations, byte-only and widening, were killed both plainly and end to end. Only the declared same-output patch control passes.
- All three act arguments are unchanged and re-derive independently.
- All four check commands are green.
- No over-attribution or adoption claim remains.

The four new findings are notes, n10–n13. Two are selftest-rigor gaps, with three surviving builder mutants. The other two are about scope outside the drafts and patch output: the patch file's own bytes, and the base or installed policy. None makes a stated `--check` guarantee false for a draft or the patch output, and none changes an act argument.

Verdict: CONFIRM WITH EXCEPTIONS
