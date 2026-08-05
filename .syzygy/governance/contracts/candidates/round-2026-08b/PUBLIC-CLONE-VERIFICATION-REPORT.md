# Public-clone verification — round 2026-08b

> **Non-authoritative round record.** Supersedes
> `../round-2026-08/PUBLIC-CLONE-VERIFICATION-REPORT.md`, which is
> banner-marked. Every figure below was produced in the session that wrote
> this file, inside a real clone, not in the working tree.

## Method

```sh
git clone <repo> <scratch>/clone2
cd <scratch>/clone2
```

Clone of commit `864718c`. The owner's working tree was not read from inside
the clone; every command below ran with the clone as its working directory.
Environment: Python 3.10.12, stdlib only, no network. `grep` on this machine
is **ugrep 7.5.0**, so every load-bearing sweep used Python `re`.

## What a clone contains

[Observed] **211 tracked files.** `_bootstrap/` is absent, as intended — it
is git-excluded, and its absence is what makes the "no artifact requires
reading it" rule meaningful rather than decorative.

## The five act arguments, computed inside the clone

| Act | Subject | Argument as computed in the clone |
|---|---|---|
| 1 | `ACTIVE-CONTRACT-MANIFEST.txt` | `ac07a06497cd72b8dd10a9a42776a6a41d7c45740ffec7905d4c27fbe7146b4f` |
| 2 | `craft-and-care/testing-and-verification.md` | `3858820f64768ef20e6514fe8adb28076263f071ac77e66a5520a612f3bcb26d` |
| 3 | `topology-candidates/BUNDLE-MANIFEST.md` | `7a3b22494a08d888901c1f0cec76833dc926e89b6f510b5abf8963071fbaeb45` |
| 4 | `intent/OVERVIEW.md` | `01d629515993188338f6a0e2d84d67543d8569003759a7c8f571a90b129c7cd1` |
| 5 | `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` | `e973e8e025c93b5d1e59d16d8661b0ae1f9804304c8f8de8957950acf3d8f9c9` |

[Observed] All five match the arguments the acceptance record offers. A
reader with nothing but the clone can verify every act before performing it.

[Observed] `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` run from the clone's
package directory: **32 of 32 OK**.

## The full battery, inside the clone

| Command | Result |
|---|---|
| `scripts/check_governance.py` | 20 OK, 9 WARN, 1 FAIL over 30 checks |
| `scripts/check_governance.py --selftest` | 10 fixtures, 0 failing |
| `candidates/scripts/verify_final_prespec.py` | PASS |
| `candidates/scripts/build_contract_index.py --check` | no drift |
| `candidates/scripts/build_dependency_index.py --check` | no drift |

The single FAIL was CG-1b, naming the two round records that did not exist at
clone time — this file and the readiness report. Both were written
immediately after, in the working tree; **a reader re-running the clone at a
later commit should expect 0 FAIL and must not take this row on trust.**

[Observed] `context_load.py` runs from the clone and resolves `doctrine:` and
`craft:` prefixes against the clone's own canonical homes: fixture 1's
declared mandatory set measured **13,842 words / 18,686 estimated tokens**,
matching the corrected fixture exactly.

## Founder-machine paths — 37 lines, enumerated rather than rounded

A Python `re` sweep for `/home/<user>/` and `~/.claude/` across all 211
tracked text files found **37 lines**. They are not one population:

| Class | Lines | Disposition |
|---|---|---|
| Raw reviewer output, stored verbatim | 22 | **Correct as-is.** A reviewer recording the path they ran from is evidence. Editing it would destroy the record the allowlist exists to protect |
| The substrate lock explaining the problem it solves | 3 | Correct — the lock names the unresolvable path in order to replace it |
| Historical round records and the rev9 findings file | 5 | Correct — they record a defect that existed |
| The checker's own self-test fixture | 1 | Correct — it constructs a founder-local pin to prove CG-19 detects one |
| **The live routing matrix and its working parts** | **5** | **Defect, fixed this session.** Three "Enumeration method" notes in `SURFACE-CLAUSE-ROUTING-MATRIX.md` and two in `matrix-parts/` gave an absolute working directory. Now package-relative |
| **`craft-and-care/README.md:18`** | **1** | **Was the last live one.** It named the machine path as where the adopted engineering bar lives. Now retained as provenance for *where the text was read*, followed by a pointer to `GOVERNANCE-SUBSTRATE-LOCK.yaml`, which pins the same material to a public repository, commit, and digests |

After the fixes, **no live artifact directs a reader to a path only the
founder machine has.** The remaining 31 lines are records of history,
evidence, or the lock's own explanation — each enumerated above rather than
summarized as "acceptable."

## What this report does not establish

- **It does not establish that the contracts are correct**, only that they
  are reproducible. Reproducibility is the cheaper half.
- **It does not establish that a clone can *act*.** The acts are chat-phrase
  ceremonies performed by the owner; what a clone gives is the ability to
  verify each argument before the phrase, which CG-7 does mechanically.
- **`semantic-equivalence-fixtures.md` was not re-run.** Its commands are
  written for GNU grep and `grep` here is ugrep; F-EQ-4 and F-EQ-8 remain
  [Unknown] on this machine until run under a real GNU grep.
