# Round 2026-08k — Capability 1 specification review binding

The three Pass 2 fresh-context reviews (RS-1 comprehension, RS-2
behavior/testability, RS-3 authority/coverage) are bound to commit
`7685939` and to these exact bytes (sha256, scripted this session):

```text
727fc3b35bb3eb09ccede6d08cbc829ea0044b031816d47842ec2573bff99290  .openspec.yaml
ac6984d2322a33da0191c6dbf9746e66d36274ef3a965008224d40d9d3a59ad5  proposal.md
a7a90828ed51fd5e98d8cbc9f35f2aa88b5cdd75f6a53f905b816dcc11267652  design.md
542c13369bc8add340829134de49dae342e01d8201e4c19568db236877cfb05c  tasks.md
7ab214c84e5b8f32bf4898052727ecd808a1c0101425f2b9cdd81e14eeff9dc0  CAPABILITY-COVERAGE.md
ff480d596f7a5434d5194318fd19fd1ff29d817d4ee75360a0295bcb5e3ba876  CONTRACT-COVERAGE.md
7deeb3ed5a6d24d1a86a1f9025b5394f4c5af4248b672ecb48880ba8c1c56bd2  GOVERNING-DEPENDENCIES.md
34f4759eb1a4e2a3dc981222059e3c47a71482fb53f78e13e516fc5471d358eb  specs/project-registration-and-honest-shape-visibility/spec.md
```

Paths are relative to
`openspec/changes/project-registration-and-honest-shape-visibility/`.
Any edit to these files after the reviews retires the reviews
(verification rule 10); the Pass 3 repair batches every accepted finding
into one edit, followed by the one Pass 4 confirming review of the
repaired bytes. Raw reviewer output is stored verbatim in `reviews/`,
never edited; verdict words are copied exactly.

## Pass 3 — the one consolidated repair (2026-08-20)

The repair batch was applied after all three reviews were stored. **The
edits retire RS-1, RS-2, and RS-3 against the current bytes**
(verification rule 10) — the three reviews remain valid records of the
commit-`7685939` bytes only. The batch took: all five blockers (RS-2
B1–B3, RS-3 B1–B2), all ten non-blocking observations worth taking
(RS-1 #1–#5, RS-2 #1–#5, RS-3 #1/#3/#4/#5; RS-3 #2 became queue row
P-49 rather than a spec edit), plus one repair the reviews did not
find: the `build_capability_1_views.py` selftest fixtures still
anchored on the pre-launch-decision `blocking_decisions` literal
(4 fixtures silently no-opping since the Pass 1 charter edit;
re-anchored, 21/21 green).

The **Pass 4 confirming review** is bound to these repaired bytes
(sha256, scripted this session; same relative paths):

```text
727fc3b35bb3eb09ccede6d08cbc829ea0044b031816d47842ec2573bff99290  .openspec.yaml
a9e170909acb672d7c46d02a6a8456511680feef4ef994ab5c297315961b735e  proposal.md
a7a90828ed51fd5e98d8cbc9f35f2aa88b5cdd75f6a53f905b816dcc11267652  design.md
bfa608b6204c9cdd6e25e5c45f0350742cb49ddbba4a0496e77b336d361ecb3b  tasks.md
2f6f4de4650b6800b968d243dd5887919ea7d4da550413db570d6928ac7646e9  CAPABILITY-COVERAGE.md
bd43e21a5930fada26549b1f6ab16be72b9d2f622a682dd07e88fccd11af7548  CONTRACT-COVERAGE.md
25ce33a8f3e33f1a64a3cec64cb1b73f4f26bfa851a4261390751efcc20ff2f2  GOVERNING-DEPENDENCIES.md
72dc0fd9d10102f1cee0645bcbdaac4b998dcacb0d86eb15dcbd1973d2550ce3  specs/project-registration-and-honest-shape-visibility/spec.md
```

The Pass 4 review's commit is named in its raw record. If Pass 4 finds
a real blocker, the bounded workflow stops and the specification goes
to the owner with the blocker stated — no second repair pass.

## Pass 4 outcome and the owner-authorized final bounded correction (2026-08-20)

Pass 4 (RS-4) returned **REVISE**: all five Pass 2 blockers verified
repaired; one remaining blocker — CAP1-REQ-038 declared `invariant`
without the CC-SPEC-4 sweep triple (pre-existing, outside RS-2's named
set). The workflow stopped and the blocker was presented to the owner.
**The owner then authorized one final bounded correction** (instruction
of 2026-08-20): change only CAP1-REQ-038's Form line to
`state projection/query`, altering no behavior, scenario, oracle,
falsifier, warrant, or coverage. RS-4's raw record stands verbatim as
review evidence over the commit-`696a9eb` bytes; **RS-4's non-blocking
observations are deferred by the same owner instruction.**

The correction was applied and `GOVERNING-DEPENDENCIES.md` regenerated
(only its embedded spec digest changed — 42 requirements, 50
authorities, unchanged). Form census after: 7 event-response,
11 prohibition, 13 invariant, 11 state projection/query = 42 — exactly
one moved, invariant → state projection/query.

## FINAL exact-byte binding — the semantic specification artifacts

The owner adoption act (CC-SPEC-10) and the one targeted confirmation
bind to these exact bytes (sha256, scripted this session; paths
relative to `openspec/changes/project-registration-and-honest-shape-visibility/`):

```text
727fc3b35bb3eb09ccede6d08cbc829ea0044b031816d47842ec2573bff99290  .openspec.yaml
a9e170909acb672d7c46d02a6a8456511680feef4ef994ab5c297315961b735e  proposal.md
a7a90828ed51fd5e98d8cbc9f35f2aa88b5cdd75f6a53f905b816dcc11267652  design.md
2f6f4de4650b6800b968d243dd5887919ea7d4da550413db570d6928ac7646e9  CAPABILITY-COVERAGE.md
bd43e21a5930fada26549b1f6ab16be72b9d2f622a682dd07e88fccd11af7548  CONTRACT-COVERAGE.md
a00ccbf24f2e106ec3a396b8ae637097b4aaca9965548aab6d1cda0f37851c8e  GOVERNING-DEPENDENCIES.md
65b66c913cd2650881a9df8cb34a3c63b3f518041e83f45d2451980d9f1d0448  specs/project-registration-and-honest-shape-visibility/spec.md
```

**`tasks.md` is deliberately outside this binding.** It is the change's
mutable lifecycle ledger (checkbox state), not a semantic specification
artifact; CC-SPEC-10 binds adoption to "what was adopted at which
digest," and no in-force clause names the task file — a sweep of the
in-force CC-SPEC/CC-IMPACT policy text finds zero mentions of it. Its
entries may therefore record later lifecycle facts (the clean-clone
commit hash, the targeted confirmation) without retiring this binding.
Any edit to the seven bound files above **does** retire the targeted
confirmation and reopens the adoption question (verification rule 10).
