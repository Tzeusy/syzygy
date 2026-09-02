# Fresh-context confirmation review — PWB effect acts (finding-2 repair)

- [Observed] Reviewed commit:
  `48e0f5db645d1fb08e5e3a65c5e50dbcece40412`.
- [Observed] Manifest SHA-256:
  `d259c3798b2961489d31c55af09e86c9711c0cfd4e5ec626211fdc2447a54150`.

Both recomputed independently (`git rev-parse HEAD`; `sha256sum` on the
manifest at this checkout) and both match the brief exactly. Did not read
anything under `/home/tze/GitHub/butlers`. No file was edited except this
one, and no mutating git command was run.

## Scope and method

Read the prior raw review (`docs/reviews/R-PWB-EFFECT-ACTS-SECURITY-RAW.md`,
CONFIRM with two non-blocking findings at `2fda7c44`), the full diff
`2fda7c44..48e0f5db` under `.syzygy/governance/`, the repaired policy file in
full, RFC5-17's text (`contracts/rfcs/RFC-0005/consent-egress-secrets.md`
lines 202–220), and re-ran the packet generator's `--check` and
`scripts/check_governance.py`.

## Criterion 1 — diff surface is exactly the three named artifacts; consent and registry bytes unchanged

[Observed] `git diff --stat 2fda7c44 48e0f5db -- .syzygy/governance/` touches
exactly three files: `ACT-SEMANTICS.md` (+4/-2 net 2 line changes),
`PWB-EFFECT-ACTS-MANIFEST.txt` (1 line changed), and
`POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` (+21/-1). No
other path under `.syzygy/governance/` appears in the diff.

[Observed] Consent record SHA-256 at both commits (`git show
<commit>:.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md
| sha256sum`): `5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841`
at both `2fda7c44` and `48e0f5db` — byte-identical.

[Observed] Adapter-registry entry SHA-256 at both commits (same method on
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`):
`d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7` at both
commits — byte-identical. Criterion 1 fully satisfied.

## Criterion 2 — policy still valid JSON, `policyVersion` bumped, `unclassifiable-excluded` named in a structurally distinct place

[Observed] `python3 -c "import json; json.load(open(...))"` parses the
current policy file without error.

[Observed] `policyVersion` = `"1.0.0-candidate.4"` (policy line 4), matching
the diff's bump from `.3`.

[Observed] The repair adds two new top-level object keys, siblings of
`matchAction` rather than nested inside it:
- `unclassifiableExclusion` (lines 109–121): `"redactionClass":
  "unclassifiable-excluded"` (line 112) — its own object, scoped by
  `appliesTo` to "every artifact excluded by classificationOrder step 5 for
  a reason other than a detector match" (line 110), i.e. the
  `sourceAdmission.unclassifiableAction` / classificationOrder-step-5 path
  the prior review's finding 2 identified as unlabeled.
- `redactionClasses` (lines 122–127): a dedicated closed-vocabulary
  declaration block: `"vocabulary": "closed by RFC5-17: excluded-artifact,
  redacted-span, unclassifiable-excluded"` (line 123), `"emitted":
  ["excluded-artifact", "unclassifiable-excluded"]` (line 124),
  `"neverEmitted": ["redacted-span"]` (line 125).

Both new fields are structurally distinct from `matchAction.redactionClass`
(line 99, unchanged, still `"excluded-artifact"`, still scoped to detector
matches only). Finding 2 is closed: the policy now gives the unclassifiable
path its own explicit label and a top-level vocabulary declaration, rather
than leaving `unclassifiable-excluded` unnamed.

## Criterion 3 — no fail-open path introduced; RFC5-17 vocabulary matches exactly; `redacted-span` non-emission is consistent

[Observed] `retainBody: false` appears in both `matchAction` (line 107,
unchanged) and the new `unclassifiableExclusion` (line 120) — no path sets
it true.

[Observed] `rawBodyHandling` (lines 137–143) is byte-unchanged from the
prior version: `storage`/`logging`/`rendering`/`machineResponse`/
`externalEgress` all `"never"`, unconditional (not nested under either
exclusion block), so it still covers both the detector-match and the new
unclassifiable-exclusion path identically.

[Observed] RFC5-17 quoted verbatim (`contracts/rfcs/RFC-0005/
consent-egress-secrets.md` lines 205–207): "Redaction classes are closed:
`excluded-artifact` (whole artifact withheld), `redacted-span` (artifact
retained, matching spans replaced by markers with a count),
`unclassifiable-excluded` (fail-closed default)." The policy's
`redactionClasses.vocabulary` string — "closed by RFC5-17:
excluded-artifact, redacted-span, unclassifiable-excluded" — reproduces this
three-member closed set exactly, in the same order.

[Observed] Consistency check on `neverEmitted: ["redacted-span"]`: RFC5-17
(lines 212–214) states `excluded-artifact` and `unclassifiable-excluded`
"withhold the artifact entirely," while `redacted-span` alone "retains the
artifact with counted markers." The policy has exactly two action sites,
`matchAction.action` (line 98) and `unclassifiableExclusion.action` (line
111), and both are `"exclude-whole-artifact"` — there is no detector or
admission path in this policy that produces a retained-with-markers result.
Given that, `redacted-span` being listed as never emitted is internally
consistent: the policy simply contains no code path capable of emitting it,
and RFC5-17 does not require every policy to use all three classes, only
that the vocabulary be closed and each emitted class behave per its
definition. `unknownRendering` (line 126) correctly states both emitted
classes "withhold the whole artifact, so every claim that depended on it
renders Unknown with reason excluded-content" — matching RFC5-17 line 213's
`excluded-content` / RFC2-24 #7 mapping. No fail-open path found.

## Criterion 4 — ACT-SEMANTICS.md and manifest quote the new digest; consent/registry digests unchanged

[Observed] Directly computed `sha256sum` on the current policy file =
`513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61`.

[Observed] `ACT-SEMANTICS.md`'s row 2 (act-semantics table) and its "Exact
phrases" block both cite `513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61`
for `approve-policy` / `APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION
POLICY` — matches the computed digest exactly, and `policyVersion` in the
same row reads `1.0.0-candidate.4`, consistent with the file.

[Observed] `PWB-EFFECT-ACTS-MANIFEST.txt`'s policy row carries the same
digest, `513a3be75bbd417a06d475c46bb423393ac59013e307157357083f29781a2a61
.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`
— matches.

[Observed] The consent (`5d705d75…`) and registry (`d71eadb6…`) rows in both
`ACT-SEMANTICS.md` and the manifest are byte-identical to the prior
version (unchanged in the diff at criterion 1), and match the directly
recomputed SHA-256 of those two files at `48e0f5db` (criterion 1). All three
digests cross-check consistently.

## Criterion 5 — script output

[Observed] `python3 scripts/build_pwb_effect_acts_packet.py --check` final
line: `CHECK OK: 3 rows verified; .syzygy/governance/contracts/candidates/pwb-effect-acts/PWB-EFFECT-ACTS-MANIFEST.txt
matches regeneration`.

[Observed] `python3 scripts/check_governance.py` final summary line: `33
OK, 19 WARN, 0 FAIL (52 checks) — counts derived, not asserted`. Output was
read in full (not just the final line/exit code); the WARN rows present
(CG-22b, CG-23, CG-24, CG-25 downgrades) are pre-existing, unrelated to the
PWB artifacts, and carry their own documented rationale (allowlists,
report-only status, selftest-coverage disclosure, advisory downgrades
pending unrelated policy adoption) — none references the PWB
effect-acts materials or the repaired policy file. 0 FAIL.

## Criterion 6 — no implementation/body-read/write/egress/execution/deployment/release authority; no state-(2) claim

[Observed] `ACT-SEMANTICS.md` lines 52–54 (unchanged by this diff) still
read: "None grants PWB implementation authority (task 1.8), write, egress,
execution, deployment, release, recovery, mission, second-repository,
autonomous or multi-user authority." Line 25 (unchanged): "A record claiming
state (2) cannot be produced by this packet."

[Observed] The new policy fields (`unclassifiableExclusion`,
`redactionClasses`) add only classification/retention vocabulary — no new
`authorizationModes`, `accessBoundary`, or scope field was touched by the
diff (all remain at their pre-repair values, confirmed by the diff itself
showing no changes outside lines 106–127 of the policy file). Neither new
field mentions implementation, write, egress, execution, deployment,
release, or "verified"/"state (2)" status. Criterion 6 holds.

## Findings summary

| Severity | Criterion | File | Line(s) | Disposition |
|---|---|---|---|---|
| — | 2 | `POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` | 109–127 | Prior finding 2 (RFC5-17 vocabulary incompleteness) is **closed**: `unclassifiable-excluded` is now named in its own structurally distinct `unclassifiableExclusion` block and in a dedicated `redactionClasses` closed-vocabulary declaration, separate from `matchAction`. |

No new defect found. No fail-open path introduced; digests cross-check
exactly across `ACT-SEMANTICS.md`, the manifest, and direct `sha256sum`;
the consent record and registry entry are byte-identical across both
commits; both governance scripts report 0 FAIL with their final summary
lines quoted above; no authority beyond the previously-reviewed
consent/policy/registry scope is claimed anywhere in the repaired bytes.
The prior review's other conclusions (criteria A/B/D/E/F/G/H in the raw
review, and its non-blocking note 2 about `ACT-SEMANTICS.md` not being
digest-pinned inside the phrase itself) are unaffected by this diff and
still hold — this diff touches none of the artifacts or logic those
conclusions were about.

**VERDICT: CONFIRM**
