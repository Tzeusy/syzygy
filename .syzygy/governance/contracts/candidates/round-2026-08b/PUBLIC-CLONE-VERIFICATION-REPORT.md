# Public-clone verification — round 2026-08b

> **SUPERSEDED — historical round record (marked 2026-08-10).** Later rounds
> regenerated the topology and overview act arguments, so the digests below
> record what was verified then, not what is offered now; do not act from
> this file. It in turn supersedes
> `../round-2026-08/PUBLIC-CLONE-VERIFICATION-REPORT.md`, which is
> banner-marked. Every figure below was produced inside a real clone, in the
> session that wrote this file, and recomputed after the last commit the
> report describes — not carried forward from an earlier clone.

## Method

```sh
git clone <repo> <scratch>/clone6
cd <scratch>/clone6
```

Clone of commit `c4f54e6`. The owner's working tree was not read from inside
the clone; every command below ran with the clone as its working directory.
Environment: Python 3.10.12, stdlib only, no network. `grep` on this machine
is **ugrep 7.5.0**, so every load-bearing sweep used Python `re`.

**A prior version of this file was written at commit `864718c` and then had
its act-1 digest edited in place when the manifest moved.** That left a report
claiming to describe one commit while quoting an argument from another — the
precise failure the whole round is about. It is replaced rather than patched,
and the lesson is recorded: **a clone report is only ever valid for the commit
it was run at.** Re-run it; do not edit its figures.

## What a clone contains

[Observed] **219 tracked files.** `_bootstrap/` is absent, as intended — it is
git-excluded, and its absence is what makes the "no artifact requires reading
it" rule meaningful rather than decorative.

## The clone found a defect the working tree could not

[Observed] At an earlier commit this round the battery **diverged**:
`check_governance.py` reported 0 FAIL in the working tree and 1 FAIL in the
clone. CG-14 found that
the acceptance ceremony's step 5 named `_bootstrap/` as a location — which
exists on the founder machine and in no clone — and the check had answered
from the local filesystem, so it read the step as executable here and
unexecutable there.

Both halves are fixed. The ceremony's step 5 now ends at the
commit and tag, with the mirror stated as founder-machine-only and explicitly
outside the ceremony. CG-14 now parses git-excluded roots from `.gitignore`
and treats them as absent on every machine, with a selftest fixture that
passes `_bootstrap/` in as *present* so the fixture fails unless the check
refuses the local answer.

This is the report's most useful result. A verification run that only ever
reproduces what the founder machine already said is not verification.

## The five act arguments, computed inside the clone

| Act | Subject | Argument as computed in the clone |
|---|---|---|
| 1 | `ACTIVE-CONTRACT-MANIFEST.txt` | `ac07a06497cd72b8dd10a9a42776a6a41d7c45740ffec7905d4c27fbe7146b4f` |
| 2 | `craft-and-care/testing-and-verification.md` | `7a716090bc827121b3f70c4f7e252fc5680cd8a56d7b4121b70f3673489690a0` *(recomputed 2026-08-06; this row previously held the retired `3858820f…`, which review RD-6 finding H-1 found unexamined by any check)* |
| 3 | `topology-candidates/BUNDLE-MANIFEST.md` | `7a3b22494a08d888901c1f0cec76833dc926e89b6f510b5abf8963071fbaeb45` |
| 4 | `intent/OVERVIEW.md` | `01d629515993188338f6a0e2d84d67543d8569003759a7c8f571a90b129c7cd1` |
| 5 | `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` | `e973e8e025c93b5d1e59d16d8661b0ae1f9804304c8f8de8957950acf3d8f9c9` |

[Observed] All five match the arguments the acceptance record offers. A reader
with nothing but the clone can verify every act before performing it.

[Observed] `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` run from the clone's
package directory, tallied by result rather than eyeballed: **32 OK, 0
FAILED** — 32 of 32 entries.

## The full battery, inside the clone

| Command | Result |
|---|---|
| `scripts/check_governance.py` | 24 OK, 9 WARN, **0 FAIL** over 33 checks |
| `scripts/check_governance.py --selftest` | 46 fixtures, 0 failing |
| `candidates/scripts/verify_final_prespec.py` | PASS |
| `candidates/scripts/build_contract_index.py --check` | no drift |
| `candidates/scripts/build_dependency_index.py --check` | no drift |

[Observed] Identical to the working-tree run at the same commit, check by
check. That agreement is the claim; it did not hold one commit earlier.

[Observed] `context_load.py` runs from the clone and resolves `doctrine:` and
`craft:` prefixes against the clone's own canonical homes. Fixture 1's
declared mandatory set measures **13,842 words / 18,687 estimated tokens**,
matching the figure the fixture records — and CG-18 recomputes that from the
declared set rather than trusting it, over 16 measurements across all eight
fixtures.

## Founder-machine paths — 37 lines, enumerated rather than rounded

A Python `re` sweep for `/home/<user>/` and `~/.claude/` across all 219
tracked files found **37 lines in 16 files**. They are not one population, and
the classification below accounts for every line:

| Class | Lines | Files | Disposition |
|---|---|---|---|
| Raw reviewer output, stored verbatim | 23 | 9 | **Correct as-is.** A reviewer recording the path they ran from is evidence. Editing it would destroy the record the allowlist exists to protect |
| Round records describing the defect, including this file | 5 | 3 | Correct — naming the bad path is how the report says it was bad |
| The checker's own selftest fixtures | 4 | 1 | Correct — they construct founder-local locators (`/home/tze/…`, `~/.claude/…`) as inputs the check must reject. Three of the four are new this commit: CG-19 previously detected only the *absence* of a URL, so a machine path sitting beside a real repository URL passed |
| The substrate lock explaining the problem it solves | 3 | 1 | Correct — the lock names the unresolvable path in order to replace it |
| The rev9 adversarial findings file | 1 | 1 | Correct — it records a defect that existed |
| `craft-and-care/README.md:19` | 1 | 1 | **Retained deliberately**, as provenance for *where the text was read*, immediately followed by a pointer to `GOVERNANCE-SUBSTRATE-LOCK.yaml`, which pins the same material to a public repository, commit, and per-file digests |

[Observed] **No live artifact directs a reader to a path only the founder
machine has.** The routing matrix and its working parts, which held five such
lines earlier in this round, now hold zero — confirmed by this sweep's file
list, which does not include them.

The count has moved twice this round — 37 over 211 tracked files, then 35,
now 37 again over 219. Each figure was correct for its commit and none
transfers. The movement is not drift: the routing-matrix and craft-README
fixes removed six, and the CG-19 rebuild added three *deliberately*, as
fixtures that feed the check a founder-local locator to prove it rejects one.
A sweep total is a measurement, not a target, and a falling number is not by
itself the goal.

## What this report does not establish

- **It does not establish that the contracts are correct**, only that they are
  reproducible. Reproducibility is the cheaper half.
- **It does not establish that a clone can *act*.** The acts are chat-phrase
  ceremonies performed by the owner; what a clone gives is the ability to
  verify each argument before the phrase, which CG-7 does mechanically.
- **It does not establish that the ceremony has no remaining local
  dependency** — only that CG-14 now finds one class of them, over the 11
  directory paths the ceremony section names. A dependency expressed some
  other way would still pass.
- **`semantic-equivalence-fixtures.md` was not re-run.** Its commands are
  written for GNU grep and `grep` here is ugrep; F-EQ-4 and F-EQ-8 remain
  [Unknown] on this machine until run under a real GNU grep.
