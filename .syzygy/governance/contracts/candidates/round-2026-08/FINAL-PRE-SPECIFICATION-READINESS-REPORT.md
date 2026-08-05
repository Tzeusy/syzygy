> # Historical — round record, not a current offering
>
> **Do not read a digest here as an act argument.** Its readiness answer is round 2026-08's, given over a corpus that has since changed twice. Successor: `../round-2026-08b/FINAL-PRE-SPECIFICATION-READINESS-REPORT.md`. Current arguments
> come from `ACTIVE-CONTRACT-MANIFEST.txt` and
> `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, never from a round record.

# Final pre-specification readiness report — 2026-08-05

Answers the round charter's five completion tests with evidence, then states
what readiness the evidence supports and what it does not. Claims are labeled
`[Observed]` (measured or reproduced here), `[Inferred]` (reasoned from
observations), `[Unknown]`.

**Headline.** Tests A, B, D and E pass with evidence. Test C passes at 11.0%
of the corpus. **Readiness is nevertheless conditional**, on two things no
report can supply: four owner acts that have not happened, and one
fresh-context review over the current bytes that was never run (§7).

---

## Test A — 30 seconds, README alone

**PASS.** `[Observed]` Independently verified by reviewer RB-1, which read
the root README with no other context and answered all four questions from it
(`reviews/RB-1-fresh-engineer-RAW.md`, "Test A — 30 seconds, README alone:
passes on all four questions").

| Question | Answered at | Evidence |
|---|---|---|
| What Syzygy is | `README.md` thesis | "A specification-driven control plane for software projects: humans define what should be true, evidence shows what is true, and agent fleets do bounded work to close the difference — with the difference always rendered honestly." Plus the artifact answer added after review: a local-first daemon with a browser application, none of it built |
| Why it exists | `README.md` "Why it exists" | Oversized diffs, scattered completions, no coherent account of what changed or whether it matched intent; underspecification surfacing after deployment |
| Current stage | Stage banner, line 1 of the body | Pre-implementation; no application code; the boundary stated as a rule, not a caveat |
| Where to read next | Eight-item start-here list | Each item names the file and what it answers |

**Budget** `[Observed]`: README 802 words (trigger 1,200); AGENTS.md 1,500 —
**at** its trigger, not under it, after the round-close additions to its
verification-hazard list. Measured by `wc -w` and reported by
`check_governance.py` CG-8, which treats the figure as a decomposition prompt
rather than a failure. The next addition to that file must remove something.

**Gap accepted knowingly** `[Observed]`: adopted doctrine cites a "README
glossary" that does not exist (RB-1 F6). The citation sites are inside
adopted doctrine, so repairing them is a doctrine amendment, not a round fix
— register item P-20.

---

## Test B — 10 minutes, following the start-here order

**PASS on all six.** `[Observed]` RB-1 restated each in its own words from the
documents alone, without the authoring conversation:

1. **Desired vs observed vs execution state** — three kinds of fact the
   system refuses to let collapse: what a human said should be true, what is
   actually true of the artifact and backed by a durable identified artifact,
   and the audit trail of what was scheduled and ran.
2. **Polaris, Trajectory, Orrery, Mission Control** — each reached from the
   overview with its literal subtitle and its owning contract.
3. **Why merged work is not proof** — doctrine's three-state thesis: work is
   never proof; a merge is execution-state evidence about *activity*, never
   observed-state evidence about *behavior*.
4. **What Syzygy may write** — VIS-5: direct writes only in `openspec/**` and
   `.syzygy/**`; everything else through adapters, consented and revertable.
5. **What is not yet implemented** — the README's explicit
   "what is not implemented" section, corroborated by `PROJECT-STATUS.md`.
6. **Governing rules** — VIS-1…7 and SEC-1…5 reachable by identifier.

**Vocabulary reachability** `[Observed]`: RB-1's term-resolution table found
every term on the default reader path either defined inline or resolvable in
≤2 hops, with four marked *marginal* (`warrant`, `SDR §1–2`, `snapshot
identity`, `genome-complete`) and one wrong-target (`D3`, since repaired).

---

## Test C — bounded task, compiled context packet

**PASS.** `[Observed]` Executed in full by RB-5 against the task *"Propose how
Trajectory should render a work item whose verification evidence is missing"*
(`reviews/RB-5-context-compiler-RAW.md` §4).

| Required dimension | Answered from | Result |
|---|---|---|
| Applicable doctrine | `trust-and-evidence.md`, `security.md` | ✓ |
| Evidence rules | RFC-0002 rendering vocabularies, RFC-0008 module 2 | ✓ |
| Relevant contract | RFC-0008 (Trajectory), selected by `applies_to` | ✓ |
| Future OpenSpec requirement boundary | RFC8-32 phase rule | ✓ |
| Accessibility and security obligations | CC-VIZ-4 (craft), SEC-2/SEC-5 | ✓ |
| Owning authority | Named per source | ✓ |

**Cost** `[Observed]`: a 4-module, 13,551-word packet — **18,293 estimated
tokens, 11.0% of the corpus**, under the 20,000-token §11.4 trigger, no waiver
needed. The full corpus was neither loaded nor needed.

**What running the test revealed** `[Observed]`, and this matters more than the
pass: a packet compiled by following the routing indexes *literally* would
weigh 23,950 tokens — **above** the trigger — and would still be unable to
state the accessibility or the security obligation, because none of the eight
reader-map rows routes a doctrine or craft source for a surface task
(RB-5 F11). The warrant-scoped packet is 5,657 tokens smaller *and* complete.
A doctrine/craft column on the eight rows would close this; it is not closed
today, and is carried as a next-pass item.

`[Observed]` A second structural finding: RFC11-1 requires a packet to name
"the exact doctrine rules included, by identifier", but doctrine selection
granularity is file-level, so including VIS-2 by identifier means loading a
whole 2,156-word file or disclosing that the rule's own text is absent. RB-5
chose disclosure. Clause-granular doctrine projection is the natural next
increment to `build_contract_index.py`.

---

## Test D — clone equality

**PASS.** `[Observed]` Verified twice: first against a simulated clone at
final bytes, then against a **real `git clone` of the pushed remote** at commit
`f2d202c` — 190 tracked files, `_bootstrap/` absent, in a directory that never
held the authoring session. Full evidence in
[`PUBLIC-CLONE-VERIFICATION-REPORT.md`](PUBLIC-CLONE-VERIFICATION-REPORT.md);
summary in `FINAL-OWNER-ACCEPTANCE-RECORD.md` §5:

- All four act digests recompute from clone bytes and match what is offered.
- `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` — 32/32 OK.
- Topology member digests vs `BUNDLE-MANIFEST.md` — 9/9 OK.
- `build_contract_index.py --check`, `build_dependency_index.py --check` — no
  drift. `verify_final_prespec.py` — PASS.
- `check_governance.py` — **15 OK, 7 WARN, 0 FAIL** over 22 checks from the
  real clone, identical to the working tree. (The earlier filesystem-copy
  simulation reported 14 OK / 8 WARN, the difference being CG-11 correctly
  Unknown where git was unavailable.)
- `context_load.py` resolves its `doctrine:` and `craft:` prefixes to
  canonical homes from clone bytes — 5,256 words / 7,095 est. tokens on the
  documented example.

**One portability defect found and fixed by this test** `[Observed]`:
`check_governance.py` previously aborted after a single WARN when `git` was
unavailable, running none of its other checks. It now degrades to a
filesystem walk, runs every check, and reports CG-11 as Unknown rather than
passed — the difference between "we could not look" and "we looked and it was
clean." A real clone is a git checkout and never hit this, but a downloaded
archive would have received a one-line silent non-answer.

**The earlier clone review's digests differ, and should** `[Observed]`: RB-8
recomputed `5c4d6798…` (act 1) and `89279260…` (act 3) from the tree as it
stood mid-round. Both are now stale, because RB-8's own blocking finding drove
the fix batch that changed them. This is the audit trail working, not a
contradiction.

---

## Test E — no hidden semantic dependency on `_bootstrap/`

**PASS.** `[Observed]` Two independent sweeps, both in Python `re` (never
shell `grep`, per the recorded ugrep hazard):

- RB-8's mid-round sweep: 61 files, 166 occurrences; 60 of 61 files properly
  marked historical or unavailable.
- This report's final-bytes sweep of the clone simulation: **74 files, 209
  occurrences**, classified by `check_governance.py` CG-12 as **38 citations
  examined, 0 findings** — no `_bootstrap/` path is cited as a *required*
  source anywhere. CG-12b lists the 50 allowlisted files with the reason each
  is exempt.

The classification buckets `[Observed]`: frozen packet history and
clause-migration provenance (which cite rev9 sources by construction); raw
reviewer output, stored verbatim and never edited — including reviewers
recording that they deliberately did *not* read the tree; round process
records, each carrying a file-level disclosure that the pointers are
git-excluded; and rule text *about* the exclusion, which is not a dependency.

`[Inferred]` Every active current-state and candidate artifact remains
understandable and reviewable without the tree. The strongest single piece of
evidence is that RB-1, RB-5 and RB-8 each reviewed from clone-equivalent
material and produced substantive, specific findings — several of them
findings the authoring session had missed.

---

## 6. What the round measured

| Surface | Words | Note |
|---|---|---|
| `README.md` | 802 | under the 1,200 trigger |
| `AGENTS.md` | 1,500 | **at** the 1,500 trigger, not under it |
| `PROJECT-STATUS.md` / `CONTRIBUTING.md` / `SECURITY.md` | 709 / 550 / 582 | new this round |
| `.syzygy/intent/OVERVIEW.md` | 1,430 | four-layer progressive disclosure |
| Active contract corpus | 99,094 across 32 modules | above the 35–50k target band; `verify_final_prespec.py` prints this as a standing owner-facing justification requirement, not a failure |
| Doctrine / craft / topology | 7,783 / 9,428 / 6,914 | adopted / owner-approved+1 gated amendment / candidate |

`[Observed]` The Test C packet was 11.0% of the contract corpus. **That ratio,
not the corpus total, is what the compaction work was for**: the corpus is
still large, and the answer to largeness is selection, which now has a
contract (RFC-0011), fixtures, and one worked end-to-end demonstration.

---

## 7. Readiness — what the evidence supports, and what it does not

`[Observed]` **Supported.** The front door is clear and measured. The
vocabulary is canonical *as a proposal* (30 terms, T-01…T-30). Candidate and
accepted artifacts are clone-visible with typed banners. The Context Compiler
contract is fixture-tested — 8/8 measurements and 7/8 digests reproduce on a
machine that never saw the authoring session. Validation is portable,
stdlib-only, and runs in docs-only CI. Every act argument is machine-checked
wherever it is quoted (CG-7a/b/c/d).

`[Observed]` **Not supported — four owner acts have not happened.** Acts 1–4
are offered, unperformed. Act 5 is optional and unresolved. The
knowledge-hygiene policy (P-12), the license (P-14), and the term registry
(P-16) are candidates with no act offered at all.

`[Observed]` **Not supported — no review has bound the current bytes.** The
eight-vertical battery predates the fix batch its own findings required. The
ninth, exact-manifest review was never run: three reviewer sessions hit the
account's session limit. Mechanical verification is complete; independent
*judgment* over the post-batch content is absent. This is the round's
principal residual, disclosed at `FINAL-OWNER-ACCEPTANCE-RECORD.md` §4 and
`ROUND-DISPOSITIONS.md` §5.

`[Unknown]` Whether the 99,094-word corpus is the right size. The band was
missed by roughly 2×; the compaction report justifies each module, the budget
triggers are reported rather than enforced, and no one has yet tried to
author a real V0 specification against it. That test is the specification
phase itself.

**The honest one-line verdict:** the repository is ready for the
specification phase *as soon as the owner acts*, and not one step before —
and the owner should decide, from §4 of the acceptance record, whether to
commission one more review first.
