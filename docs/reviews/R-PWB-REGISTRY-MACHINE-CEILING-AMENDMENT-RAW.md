# Review — P-114 PWB registry machine-ceiling amendment, round 1
Reviewed commit: cd653f04dab2a5fe284a43c9da0d3e3fa540c078
Manifest SHA-256: 5396c8912cd329ba4d4413245e69c1d6fb81536713115e7ca32506e7b1768ac1
Verdict: REVISE

Reviewer: a fresh-context agent session that did not write the package. Scope: `REVIEW-BRIEF.md`
(round 1). The artifact is the package directory
`.syzygy/governance/contracts/candidates/pwb-registry-machine-ceiling-amendment/`, plus
`scripts/build_pwb_registry_machine_ceiling_amendment.py` and
`docs/evidence/syzygy-59s5-live-size-2026-10-20.json`. I read no Butlers content and started no daemon.
I edited nothing in the repository. The dry run below ran in a throwaway `git clone` under my
scratchpad.

## Answers to the six questions, in brief

1. **One value: yes.** [Observed] The subject carries `"maxMachineResponseBytes": 8388608,`
   exactly once, and the bare digits `8388608` appear exactly once. Replacing that literal gives bytes
   that differ in exactly one line (same line count). Parsed, they differ at exactly one leaf,
   `('entries', 0, 'resourceLimits', 'maxMachineResponseBytes')`. Those bytes hash to the manifest
   row. `git apply` of the shipped patch in a clean clone changes one line (`1 insertion, 1
   deletion`), and the result hashes to the row too. I derived this with my own Python, not the
   builder's.
2. **Honest basis: mostly.** The arithmetic matches the evidence record. One attribution claim is
   labelled more strongly than its evidence (Finding 2), and one disagreement in the evidence is
   dropped (Finding 9).
3. **Ledger complete: no.** The battery dry run is exact. The literal-sweep completeness claim is
   false, and one test that reads the entry's bytes is not named (Finding 4).
4. **Asks.** Ask 2 is necessary. The owner's direction says the raise "takes effect only under a
   separate implementation authorization, asked in the P-114 packet", and I confirmed the daemon
   hard-codes the value. But its "nothing else" boundary does not match what the sign-off commit must
   edit (Finding 5). The "sign without authorize" arm is safe in effect but leaves an unrecorded
   signature undefined (Finding 8).
5. **Versions.** Keeping `1.2.0-candidate.1` may be defensible. But the delta cites only the
   precedent that supports it and leaves out the entry's own contrary convention (Finding 3).
6. **Builder.** Every `--selftest` mutant fails for the predicate it names. `--check` fails closed on
   a sibling's edit. But the applied-state gate predicate refuses the very state ask 2 prescribes
   (Finding 1), and several predicates are substring checks that are easy to defeat (Findings 6 and 7).

## Findings

**Finding 1 — The applied-state `--check` refuses the gate state that ask 2 prescribes** (revise)

[Observed] The builder's applied-state gate predicate (line 201) is:

```python
if f"registry: '{CURRENT_GATE_RECORD}'" in gate:
```

`CURRENT_GATE_RECORD` is act B's record path. Ask 2 item 2, and `IMPACT-LEDGER.md` B1, prescribe
moving the "supersession target (now act B)". So after a correct implementation,
`PWB_SUPERSEDED_ACT_RECORDS` in `governance-inputs.ts` reads
`registry: '.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md',`. That
is the same substring, so the predicate fires.

I reproduced this with a probe that imports the builder and builds its own fixture. It applies the
entry, moves the constant, points `PWB_ACT_RECORDS.registry` at a new record and points
`PWB_SUPERSEDED_ACT_RECORDS.registry` at act B, which is the prescribed state. `check()` returns
`applied` with the finding "still points the registry act at …PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md:
the PWB-REQ-005 gate refuses every Butlers read".

The selftest's `_apply_fixture` never models this. It moves only the `PWB_ACT_RECORDS` line and
leaves the supersession target on the currency-briefing record. So the "applied state verifies" case
passes over a state the packet does not prescribe. The ledger says this builder's `--check` joins
the battery in the sign-off commit. As written, the correct sign-off commit would fail its own
battery line.

**Fix required:** scope the predicate to the `PWB_ACT_RECORDS` object, for example by parsing the
`export const PWB_ACT_RECORDS … = { … };` block. Better still, also require the supersession target
to equal act B. Make `_apply_fixture` produce the prescribed state, including the supersession move.
Add a mutant that leaves the supersession target unmoved.

**Finding 2 — The growth attribution is labelled Observed; the evidence record labels it Inferred** (revise)

`SEMANTIC-DELTA.md`, "Evidence or decision basis", second paragraph, opens `[Observed]` and
concludes:

> It comes from the one live input outside the git revision: the Beads Dolt read in
> `packages/three-surface-poc-core/src/work-items.ts`.

What was observed is narrower: the same 8,497,943 bytes at `0ba72000` and at `8340fa22`, against the
same Butlers revision and the same evaluation identity. "Therefore not Syzygy code and not the
Butlers git tree" is a deduction that assumes the answer is a deterministic function of those
inputs. "It comes from the Dolt read" is elimination over an input list the record asserts but does
not enumerate. The answer also carries evaluation and capture instants from `main.ts`'s clock, which
are small but are live inputs too.

The evidence record itself keeps this distinction (`growthSince20261015.attribution`): "[Inferred]
the growth is work-item rows". The delta upgrades it. The owner packet repeats it ("The growth is not
code. It comes from the live work-item read"), with the [Inferred] tag attached only to the rate.

**Fix required:**
- Split the paragraph. Keep [Observed] on the equal byte count at both commits, at the same Butlers
  revision and the same evaluation identity.
- Label the "not code / not git tree" conclusion and the Dolt attribution [Inferred], matching the
  evidence record.
- Mirror that split in `OWNER-DECISION-PACKET.md` "In one paragraph".

**Finding 3 — The version precedent is cited selectively** (revise)

The delta says:

> The 2026-10-02 re-pin act B is the precedent: it changed this entry's bytes under the same version.

[Observed] That is true of act B (`144fa5f7`): it moved only the `governingBehaviorContract` version
and signer.

But the entry's other two amendments both bumped the version:
- The `.18` currency-and-briefing amendment (`f5da19ff`) moved `registryVersion` and
  `observerVersion` from `1.1.0-candidate.1` to `1.2.0-candidate.1`. It was also a `resourceLimits`
  change: it added `maxBriefingResponseBytes`.
- Its delta, `pwb-registry-currency-briefing-amendment/SEMANTIC-DELTA.md` lines 160–164, calls the
  bump "a minor bump, matching this entry's own convention". Under that convention the 2026-09-05
  amendment moved both versions from `1.0.0-candidate.3` to `1.1.0-candidate.1`.

So the closest precedent, a Normative change to a declared limit, points the other way. Act B is the
odd one out: a pin repair with no change in behaviour.

The gate-scope argument ("a version move would widen the code change past the gate's pointers") is
real but small. [Observed] It adds the scope anchor at `governance-inputs.ts:116`,
`PWB_OBSERVER_IDENTITY.observerVersion` at `project-shape-observation.ts:50`, and a handful of test
literals. The evaluation identity changes either way, because `resourceLimitsDigest(limits)` feeds
it (see Finding 4).

**Fix required:** name both precedents and the entry's stated convention. Then argue why this
Normative limit change departs from it, or move the versions. Either outcome is acceptable. Citing
only the supporting precedent is not.

**Finding 4 — Impact ledger: a false completeness claim and an unnamed reader of the entry** (revise)

(a) **Literal sweep.** Method item 2 says "ugrep for `8 MiB` / `8 MB` adds no file outside those
73". [Observed] `git grep -l -F -e "8 MiB" -e "8 MB" 8340fa22` returns 18 files. Seven are outside
the 73-file set (`8388608 | 8,388,608 | maxMachineResponseBytes`, which I re-derived as 73 at
`8340fa22`). Of those seven, three name this machine ceiling:
- `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/OWNER-DECISION-PACKET.md`
  (lines 76, 85, 137: "8 MiB authenticated machine JSON ceilings", "The 8 MiB machine ceiling is
  larger than…");
- `docs/reviews/R-IMPL-P100-GOVERNING-INTENT-1-RAW.md:37` ("0.7726 of the 8 MiB ceiling");
- `docs/reviews/R-PWB-TRUTH-POLICY-COMPREHENSION-CONFIRMATION-RAW.md:21`.

The other four are false positives: `128 MiB`, `8 KiB`/size prose, `256 MiB`, `2.13 MB`. None of
the three needs editing (performed packet, raws). But the stated sweep result is wrong, and part A
lists the truth-policy package's SEMANTIC-DELTA while leaving out its OWNER-DECISION-PACKET (rules 2
and 9).

My first method was a Python `re` sweep over `git ls-files` (2,867 tracked, 2,863 decoded, 4
skipped). It agrees with the ledger's 40 value files at base. The current 49 are those 40, plus the
package's 7 files, the new evidence record, and the new P-114 register row in
`PENDING-OWNER-DECISIONS.md:1358`.

(b) **A reader of the entry's bytes is not named.**
`packages/three-surface-poc-core/src/project-shape-observation.test.ts:758-790` ("observer identity,
limits and failure states are byte-equal to the act-bound registry entry") reads the installed
subject. It asserts `expect(PWB_RESOURCE_LIMITS).toEqual(consumedLimits)`.

This test is the mechanism that keeps the entry and the constant in step. It fails on a patched
entry without item 1, and on item 1 without the patch. That is the strongest evidence for the
ledger's "one commit" claim, but the ledger never names it. The dry run ran only the two gate test
files, so it could not see it. `project-shape-manifest.test.ts:576` also reads the entry
(`maxIndexDepth`, unaffected).

(c) **The evaluation identity moves, and the ledger does not say so.** [Observed]
`walkthroughEvaluationIdentity` (`walkthrough-readiness.ts:106-127`) digests `deterministicInputs`.
Those include `resourceLimitsDigest(limits)` (`project-shape-observation.ts:622`) and the registry
act's identity and artifact digest. So the sign-off commit changes `pwb-eval-…` from the
`pwb-eval-5db7b3cd512bd68a19962f63` the evidence record names. Any walkthrough run record bound to
the current identity then reads `evaluation-mismatch`. [Inferred] This is expected and probably
harmless, but it is a downstream effect a reader of the ledger should be told about.

**Fix required:**
- Correct the method sentence and list the three `8 MiB` prose files in part A as unchanged history.
- Add a short "readers of the entry's bytes" table: the parity test, the manifest test,
  `governance-inputs.ts`/`walkthrough-inputs.ts` (path only), and the builders in B2.
- Either run the full vitest suite in the dry run or state its scope as "the gate's tests only".
- Note that the evaluation identity changes.

**Finding 5 — Ask 2's "nothing else" does not match what the sign-off commit must edit** (revise)

Ask 2 says "exactly the following, nothing else". Its item 4 treats four builder and recorder
successors as needing implementation authority. Yet the same commit must also make several other
edits:
- edit `scripts/check_governance.py`: the CG-7e phrase registration and `ACT_DIGEST_COPY_FILES`
  (ledger B2 row 1, called "recording, not code");
- add a new dedicated recorder script (B3, "governance tooling, not implementation");
- add the CG-26 triple (battery, hosted workflow, count sentence);
- write this package's own `--check` into the battery.

Items in the same class (scripts that verify acts) fall on both sides of the line, and the packet
does not say what rule divides them. A signing lane reading "nothing else" literally cannot write
the recorder or the registration.

Item 4's wording is also open-ended: "each accepts a later performed act's row over the subject".
Read literally, that loosens four checks of performed acts for any later act. The precedent the
ledger cites (`PERFORMED_SUCCESSORS` in the loaded-profile builder) names specific packages.

**Fix required:**
- Either bring the recorder, the CG-7e registration and the battery and CI lines into ask 2 by name,
  or state in the packet the rule that puts them outside it and cite that rule's authority.
- Narrow item 4 to "accepts this package's manifest row, named explicitly, as the later performed
  act".

**Finding 6 — "Authorize without signing: the builder fails closed" claims more than the builder enforces** (note)

The packet says "item 1 never runs ahead of the signed entry (the builder fails closed on that)".
Two things weaken that claim:
- [Observed] The builder's `--check` is not in the PROJECT-STATUS battery or the hosted workflow
  today. It joins only in the sign-off commit, so before that nothing runs it automatically.
- Its predicates are substring checks. In my probes `check()` returned clean (`[]`) in each of these
  cases:
  - P3: the constant was moved to 16777216 and `maxMachineResponseBytes: 8388608,` was left in a
    comment.
  - P4: the entry was applied with act B's pointer written in double quotes.
  - P5: the entry was applied with only the record path moved, while the act identity
    `PWB-OBSERVER-REGISTRY-ENTRY-BEHAVIOR-CONTRACT-REPIN-2026-10-02` and the recording tag stayed
    unmoved. P5 is the gate failure the predicate claims to catch.

**Fix:** reword the packet sentence so it rests on the authorization's own bounds. Either put the
builder's `--check` into the battery now (it is green unapplied) or say it does not run until
sign-off. Tighten the predicates: parse the `PWB_RESOURCE_LIMITS` object, and check act identity
and tag along with the path.

**Finding 7 — Selftest coverage gaps (rule 6)** (note)

[Observed] All 14 cases print `ok`. Each mutant's needle matches the predicate it names. Gaps:

- *"a sibling's edit to the subject makes the patch stale"* edits `maxHumanResponseBytes`, which
  sits inside the hunk's 3-line context. A sibling edit outside the context window leaves the
  regenerated patch byte-identical. In my probe P2 (a trailing space on line 3), only the manifest
  predicate caught it. `--check` does fail closed, but through the manifest. The needle "differs from
  its regeneration" matches both the patch and the manifest lines, so the selftest cannot tell which
  predicate held.
- *"the proposed bytes differ from the base in exactly one line"* is an assertion over real data,
  not a mutant. Nothing is mutated, so it cannot show that a predicate fails.
- Missing mutants: the Finding 1 supersession state; `git apply --check` failing on its own (no
  mutant isolates `_git_apply_check`); "manifest does not carry exactly one row" (unreachable while
  the regeneration comparison runs first).

**Fix:** add an out-of-context sibling mutant whose needle is `MANIFEST.txt differs`. Add a mutant
that leaves the patch byte-identical but makes it unappliable, or drop the claim that the apply
check is exercised.

**Finding 8 — "Sign without authorizing" leaves an unrecorded signature undefined** (note)

The packet says the sign-off "is **not recorded**" and "waits for the authorization". It is safe in
effect: nothing in the tree moves. But it does not say whether an owner signature given in a session
and recorded days later still binds, or must be asked again. Withdrawal-defeats-grant and VIS-4
practice argue for re-asking.

**Fix:** state that an unrecorded sign-off lapses and both asks are re-offered together, or that the
lead records nothing until both answers exist in one exchange.

**Finding 9 — The delta drops the evidence record's own disagreement** (note)

The record notes that the machine and Trajectory marginals give about 394 and 261 item-equivalents
("the two figures disagree, so changed rows … and items the board does not render are likely part
of it"). The delta presents "about 79 item-equivalents per day" from the machine figure alone. The
arithmetic checks: 570,510 / 5 = 114,102; / 1,447.06 ≈ 78.9. But the per-day item figure is less
certain than its presentation suggests.

**Fix:** add one clause carrying the disagreement.

### Numbers re-derived (all match)

[Observed] Every figure below matches the evidence record and the P-100 record:
- 8,497,943 − 7,927,433 = 570,510;
- 570,510 / 5 = 114,102 per day;
- 16,777,216 − 8,497,943 = 8,279,273, and 8,279,273 / 114,102 ≈ 72.6 days;
- 8,497,943 / 8,388,608 = 1.0130, over by 109,335;
- P-100 cost 7,927,433 − 5,373,395 = 2,554,038 ("about 2.55 MB");
- 16 MiB at 10 to 100 Mbit/s ≈ 13.4 to 1.34 s;
- `/trajectory` 1,672,253 / 2,097,152 = 79.7%.

Line citations hold:
- subject lines 271 and 281;
- `project-shape-observation.ts:82`;
- `governance-inputs.ts` lines 61, 66, 110, 113 and test lines 188, 262, 309, 311, 316;
- both `boundedResponse(..., 'maxMachineResponseBytes', ...)` calls in `routes.ts` (lines 233 and
  255);
- the weak etag and 304 in `machineHandle`, after a full `JSON.stringify(model)`.

[Unknown] Serialization time at 16 MiB, as the delta itself says.

## Checks run

- `python3 scripts/build_pwb_registry_machine_ceiling_amendment.py --check` → `pwb-registry-machine-ceiling-amendment: unapplied, verifies`
- `… --selftest` → `selftest: 14 of 14 predicates held`
- `… --digests` → the row `f2b3573c…` for the subject
- `… --manifest-digest` → `5396c891…`, and `sha256sum` of the manifest file gives the same value
- My own Python over the subject: one old literal, one changed line, one changed JSON leaf, and the
  proposed bytes hash to the row.
- Scratch clone at `cd653f04`, PROJECT-STATUS battery parsed and run line by line:
  - base: `commands 106 nonzero 0`;
  - with the patch applied: `commands 106 nonzero 7`, exactly the seven in ledger B2:
    - `check_governance.py`: `1 FAIL (53 checks)`;
    - the currency-briefing builder, `--check` and `--selftest`;
    - `record_pwb_registry_currency_amendment.py --check`;
    - `build_pwb_behavior_contract_repin.py --selftest` (`base_bytes` ValueError);
    - `record_pwb_behavior_contract_repin_acts.py --check registry`;
    - `check_spec_reconciliation.py --selftest`.
  - The patched subject hashes to `f2b3573c…` = the manifest row.
- Literal sweep (Python `re` over `git ls-files`): 2,867 tracked, 2,863 decoded, 4 skipped. 49 value
  files now; 40 at base after removing this commit's additions.
- `git grep -l -F` on the three needles at `8340fa22` → 73.
- `git grep -l -F -e "8 MiB" -e "8 MB" 8340fa22` → 18, 7 outside the 73, 3 of them real (Finding 4a).
- Builder probes (P1 to P5) over temporary fixtures built by the builder's own `_fixture`:
  - P1 → refuses the prescribed state;
  - P2 → caught by the manifest only;
  - P3, P4, P5 → clean (`[]`).
- `git log` on the subject plus `git show f5da19ff` / `144fa5f7` → `.18` bumped both versions; act B
  did not.
