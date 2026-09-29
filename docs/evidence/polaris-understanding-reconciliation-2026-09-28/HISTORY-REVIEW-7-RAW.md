# History review 7 — reconciliation recorder
Verdict: REVISE
Reviewed commit: 242493a1c8839b7eb43dd9ebdd2375aa30728cc4
- `scripts/record_polaris_understanding_adoption.py`: `9cc6154f5230aa47df48c301dd00b673c534f6637af1a5383ea79adaf71660a0`

Reviewer: independent fresh-context agent, 2026-09-29. Clone of
`/home/tze/GitHub/syzygy` with `recorder/successor-rows` fetched, checked out at
the reviewed commit. Subject: `git diff origin/main 242493a` (3 files, +154/−6).
The recorder digest above was computed with `sha256sum` in the clone [Observed].

## Criteria results

1. Fail-closed exception. The package-level gates hold, but the gate itself is
   code whose bytes no review binds (M1). Details below.
2. Adversarial cases: run as scratch-clone probes (listed below).
3. `--selftest` exits 0 with four PASS lines, including `56 trust-boundary
   mutations refused` and `PASS successor rows selftest: absent tool,
   unperformed, performed and drifted packages` [Observed]. `--check` exits 1
   with exactly `FAIL exact digest reconciliation unresolved: latest history
   review does not bind the current recorder:
   docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-6-RAW.md`
   [Observed].
4. Rule-6 rows: I re-ran the five new rows of `history-reading-rule6.json`
   (the last 5 of `mutants`). Each ran in a fresh clone at `d50197fe…`, with
   `old` occurring exactly once, `old→new` applied, and the file's `command`
   (`python3 scripts/record_polaris_understanding_adoption.py --selftest`) run.
   Result: 5/5 exit 1, 5/5 print their recorded refusal [Observed]. Guards with
   no row are listed under N4.
5. HISTORY-READING.md: accurate as far as it goes, but it leaves out the
   unbound tool (M1) and the multi-package and malformed-package behaviour
   (N1, N2).
6. `python3 scripts/check_governance.py` gives `31 OK, 21 WARN, 0 FAIL (52
   checks)`. `--selftest` gives `347 fixtures, 0 failing` [Observed].

End-to-end positive case [Observed]. In a scratch clone I performed the real
understanding package with `readability_successor.py --record` (the phrase
was the package label plus its manifest sha256). `--check --all` then reported
it as `performed-exact`. I then ran `check()` with only `history_review`
stubbed out, and it returned C1 `9322656d…`. So the exception does what the
package packet needs. The unmodified `--check` fails only on the history-review
line.

## Blocking findings

**M1 — The review binding no longer covers the subject-drift gate: it now
depends on `scripts/readability_successor.py` at today's bytes, which no review
binds.** [Observed]

- `scripts/record_polaris_understanding_adoption.py:277-284` loads
  `self.root / 'scripts/readability_successor.py'` and runs `exec_module` on it.
- `:286` and `:284` hand the grant decision to that module's
  `Package.check()` and `packages()`.
- Before this change the recorder executed no repository code. HISTORY-READING.md
  line 29 says: "**What binds the recorder now.** Its current bytes must equal
  the digest that the latest `HISTORY-REVIEW-<n>-RAW.md` in this directory
  binds."
- The tool's current sha256 is `88358478…`. A tracked-file sweep finds 0
  citations of it in full or as a 12-character prefix, so no review, act or
  manifest binds it [Observed].
- The new HISTORY-READING bullet (lines 23-28) names the tool but does not say
  that its bytes are unbound and trusted as they are today.

Probe (i) [Observed]: in a clean clone at the reviewed commit I made three
changes:
- added `return "performed-exact"` as the first line of `Package.check()`;
- appended `INJECTED` to the amendment's `proposal.md`;
- added a package `zz-x` holding only a `SUCCESSOR.json` (predecessor = the
  adopted digest `284859db…`, with no act, no aggregate block and no review) and
  a one-row manifest.

`check()`, with only `history_review` stubbed, returned `check ok`. The
recorder's own sha256 was still `9cc6154f…`, so a history review bound to these
bytes would still bind a recorder that now accepts arbitrary subject bytes.

Mitigation [Observed/Inferred]: CI runs `readability_successor.py --all --check`
and `--selftest` (`.github/workflows/governance-docs.yml:184,187`). A loosened
`check()` would probably fail the tool's own selftest unless that was edited
too [Inferred]. That makes CI a guard, not a binding.

Required, either of:
- (a) Pin the tool's sha256 in the recorder and refuse to `exec_module` any
  other bytes, so a tool change forces a recorder change and a new history
  review. Add a rule-6 row for the pin.
- (b) If the unpinned trust is deliberate, say so in the "What binds the
  recorder now" section of HISTORY-READING.md: the exception trusts
  `scripts/readability_successor.py` and the package records as they stand
  today, and no history review binds them. Make it a disclosed design choice
  rather than an implicit widening.

## Notes

**N1 — A malformed package anywhere blocks the whole check. It does not just
grant nothing.** [Observed]
- `module.packages(self.root)` (`:284`) constructs every `Package` outside the
  `try`, and `Package.__init__` raises on bad JSON or keys
  (`scripts/readability_successor.py:81-86`).
- Probe (b): an unrelated `zz-bad/SUCCESSOR.json` containing `{` raised
  `JSONDecodeError`, and one containing `[1]` raised `ValueError … keys must be
  exactly …`. Both refused the recorder even though the legitimate performed
  package was present.
- This is fail-closed. But once the understanding successor is performed,
  `successor_rows` runs on every `--check`, so a half-drafted unrelated
  successor package breaks this recorder.
- HISTORY-READING line 27-28 ("unperformed, drifted or broken grants nothing")
  and the docstring at `:272-275` ("A package that does not check as
  performed-exact grants nothing here") understate this. Escapes that are not
  ValueError/OSError from `check()` (TypeError, KeyError) reach `main`'s
  `except` at `:1083`. Anything else is an uncaught traceback with non-zero
  exit. Either way it is fail-closed.

**N2 — Several packages claiming one path: the last in sorted directory order
wins.** `:292` overwrites `rows[path]` [Observed]. I forged a second package in
a clone where the real successor was already performed. It had a foreign
predecessor and the same row, and it checked `performed-exact`:
- Probe (f), named `zz-forge`: the recorder refused with `current subject drift`.
- Probe (g), named `aa-forge`: the recorder accepted, because the legitimate
  package was read last.

A foreign predecessor is never accepted, so this is safe, but whether the check
is denied depends on directory names. A chained successor (adopted→X→Z) can
never satisfy the predecessor test, and the first package would stop checking
`performed-exact` in any case. Say this in HISTORY-READING if a second restyle
is ever expected [Inferred].

**N3 — The exception relies on working-tree act records, not on Git history.**
[Observed]
- Probe (h'), on an unperformed tree: a fabricated package passed `check()`.
  It carried a self-written act file, an appended aggregate block, a
  self-written uncommitted `Verdict: CONFIRM` raw and predecessor = adopted
  digest. With `INJECTED` appended to `proposal.md`, the recorder accepted.
- The recorder's own evidence is tied to Git: blobs at fixed commits, and
  history raws must be committed and never deleted. The successor tool asks
  none of that.
- The owner-signed manifest (`readability_successor.py:118-122`) does not cover
  predecessor digests. They are protected only by the act body's consistency
  check (`:248`). Probes (a) and (c) show that editing `SUCCESSOR.json` or the
  act alone is refused.
- This amounts to forging an owner act, which is outside what any tool here
  detects. Disclose it alongside M1.

**N4 — Guards the selftest kills but no rule-6 row pins.** I checked each by
applying the mutant once at `242493a` and running `--selftest` [Observed]:
- `except (ValueError, OSError): performed = False` → `True` (`:287-288`) is
  killed by `drifted successor granted rows`.
- `rows[path] = (package.predecessor[path], installed[path])` →
  `(installed[path], installed[path])` (`:292`) is killed by `performed
  successor row`.
- Removing the tool-absent `is_file()` guard (`:279-280`) is killed only by an
  uncaught `[Errno 2]`, which is not a named refusal.
- Replacing the `.get(path, (None, None))` default with `(digest(adopted),
  digest(current))` (`:421`) is killed by `mutation accepted: …/spec.md`.

The first two are security-polarity guards and deserve their own rows.

**N5 — Minor code notes.**
- `successor_rows` re-runs `exec_module` and every package's `check()` once per
  drifted subject (`:421` sits inside the 8-row loop). That is twice per path
  set, and again through `Frozen` (`:527-528`).
- `spec_from_file_location` (`:277`) runs before the `is_file()` test (`:279`).

Both are cosmetic.

**N6 — The HISTORY-READING figures check out** [Observed]:
- "56 mutations, was 54": origin/main's recorder prints `54 trust-boundary
  mutations refused` and the reviewed one prints 56.
- "Five more (round 7) pin … its predecessor test, its row test, the performed
  filter, the per-package gate, and the frozen view's delegation" (line 75):
  this matches rows 1-5 in order.
- The Round 6 line now records CONFIRM. That is accurate for the retained raw
  this subject's base is bound to (per the brief; I did not re-read that raw).
