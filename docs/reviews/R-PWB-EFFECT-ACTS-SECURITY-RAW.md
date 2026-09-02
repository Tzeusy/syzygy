# Fresh-context security and authority-boundary review — PWB effect acts

- [Observed] Reviewed commit:
  `2fda7c440d996a5c58e6cf8577361520a0f1dca0`.
- [Observed] Manifest SHA-256:
  `b9af93fdd25dc57b99cffd7585c8222c763a56fc142d1aa6f30f58819394c849`.

Both recomputed independently with `git rev-parse HEAD` and `sha256sum` at the
named checkout; both match the brief exactly.

## Scope and method

Read only the six named SUBJECT items, the named GOVERNING REFERENCES
(RFC-0003 both modules, RFC-0004 module 1, RFC-0005 module 2, doctrine
security.md, PWB-REQ-003/PWB-REQ-005 from the adopted spec, PWB-STATE1-AMENDMENT-ACT.md,
the general-trusted-bootstrap CONTRACT-AMENDMENT-MANIFEST.txt, and the prior
R-POLARIS-OBSERVATION-GATE-CONFIRMATION-RAW.md review), and ran the generator
script's `--selftest`, `--check`, and `--phrases`. Did not read anything under
`/home/tze/GitHub/butlers`. No file was edited except this one.

## Digest cross-checks

- [Observed] `sha256sum PWB-EFFECT-ACTS-MANIFEST.txt` = `b9af93fd…4c849` — matches brief and matches `--check`'s output ("CHECK OK: 3 rows verified … matches regeneration").
- [Observed] `--selftest` → `SELFTEST OK: 3 rows; byte, digest, path, dropped-row, stray-line and review-binding mutations rejected` (exit 0, output read, not just exit code).
- [Observed] `--phrases` output reproduces exactly the three phrases in `ACT-SEMANTICS.md` lines 38–40, argument-for-argument:
  - consent `5d705d75f993059d5ae5561b1a6f99d143462d9d2e5bcea8ecc9b0c258777841`
  - policy `680daf81c9ac5d33c09a6a4b4fa7b66a0002155fa7b4b6d03ecfcc4ba78aaae0`
  - registry `d71eadb612cf657983d96ad44415b832054dc37e51ea674e569d9b8f655d05d7`
  All three match `sha256sum` recomputed directly against the three subject files at this commit, and match the manifest rows.
- [Observed] Spec digest cited by all three artifacts, `2e453a6ec6dbc19c5df226650c6e7a94c46e81f65d9d180f57d1dc1dce7fd07e`, is exactly the spec row of `PWB-STATE1-AMENDMENT-ACT.md`'s "Signed artifacts" table (`specs/polaris-project-wide-butlers-model/spec.md` row) — the signed one.
- [Observed] RFC-0004 digest cited by the registry, `b21fc950103964c34e2f9b2d78c97ac8e03720f311738e0e6323afb29b8d6f0e`, matches both (a) `sha256sum .syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md` recomputed directly, and (b) the `rfcs/RFC-0004/general-contract.md` row of `general-trusted-bootstrap-authorization/CONTRACT-AMENDMENT-MANIFEST.txt` — the accepted current one.

## Criterion A — RFC3-16(b)'s nine items, per artifact

[Observed] `ACT-SEMANTICS.md` binds all nine items for every one of the three acts: common items 1 (project identity), 5 (owner attribution), 6 (act instant — "the instant the owner writes the phrase … never back-dates"), 8 (supersession/revocation — explicit "none: each act is the first act on its artifact"), and 9 (A1 identity — "explicitly absent … no correlation is claimed") are stated once for all three acts; per-act items 2 (stable artifact identity), 3 (exact digest), 4 (act type: `consent-observation`/`approve-policy`/`adopt-registry-entry`, drawn from RFC3-16(b) item 4's own vocabulary — "consent," "approve," "adopt"), and 7 (scope) are tabulated separately per act. No item is missing or left to inference across the nine.

Two non-blocking observations:

1. Item 6's "act instant" is correctly distinguished from the consent record's own `Statement date: 2026-08-31` (the date of the owner's quoted words, not the act) — the consent file itself makes this explicit ("the future act records its exact grant instant," line 24). No contradiction.
2. `ACT-SEMANTICS.md` is the document that *fixes the meaning* of items 4 and 7 (the act-type vocabulary and each act's scope prose) but is not itself in the three-row manifest population and is not digest-pinned inside the offered phrase (the phrase's SHA-256 argument covers only the artifact acted on, RFC3-16(b) item 3 — never `ACT-SEMANTICS.md`). An edit to `ACT-SEMANTICS.md` after a packet is generated but before the owner performs the phrase would not be caught by the phrase itself. This repo's established pattern mitigates it in practice — `PWB-STATE1-AMENDMENT-ACT.md` records a "Frozen provenance: reviewed subject: `8847feef…`" **commit** hash, not just per-artifact digests, which would transitively pin `ACT-SEMANTICS.md` too if the eventual PWB-effect-acts act record follows the same pattern — but that pattern is not demonstrated inside the candidate materials themselves (the generator's `OWNER-SIGNOFF-PACKET.md` template cites `ACT-SEMANTICS.md` only by path, not by digest — script lines 259, 274). Recommend the future act record explicitly freeze a reviewed-subject commit (as the PWB-STATE1 act did) so `ACT-SEMANTICS.md`'s meaning is provably pinned too. Non-blocking: no artifact claims otherwise, and the pattern to close this exists and is precedented in this repo.

## Criterion B — consent record (RFC3-7 / RFC5-12 / PWB-REQ-005)

[Observed] `BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md` carries RFC3-7's required fields: attribution ("Owner: Tzeusy"), scope (the "Scope" section), and is framed as individually revertable ("The owner may narrow or revoke it through a later recorded act," line 52). Consent class is `observation` (RFC5-12's closed vocabulary). PWB-REQ-005's consent-specific fields are present verbatim: observing project `project:syzygy`, configured repository `repository:butlers-configured-poc` (both at line 15, "Subject"), observation content class `declared-project-shape-text` (line 13).

[Observed] Scope excludes secrets/credentials (PostgreSQL, credential-store, secret API, `.env`/credential files — lines 45–46), execution (line 48), egress/network (line 48), writes to Butlers (line 49), and any second repository (line 50) — all five of criterion B's named exclusions are present verbatim.

[Observed] No retroactive authorization: "No future act over this candidate retroactively authorizes the body reads in `docs/reviews/R-POLARIS-PRECONDITION-READ-BOUNDARY-INCIDENT.md`" (lines 73–74) — this is exactly the fix the prior review's blocker 1 required, and it is still present verbatim in this version.

## Criterion C — secret-classification policy (SEC-5 / PWB-REQ-003 / PWB-REQ-005)

[Observed] Fail-closed semantics: `unclassifiableAction: "exclude-whole-artifact"` (line 66); `classificationOrder` step 5 excludes the whole artifact "on any match, NUL byte, strict UTF-8 failure, unknown extraction class, parse failure or resource-limit failure" (line 114); `rawBodyHandling` unconditionally sets storage/logging/rendering/machineResponse/externalEgress to `"never"` (lines 118–124) — this field is not nested inside a single detector's match action, so it covers every excluded body regardless of which classificationOrder step excluded it, satisfying "raw bodies never stored/logged/rendered/returned/egressed" for both the detector-match and the unclassifiable path.

[Observed] Hash-not-body retention: `matchAction.retainedFields` = `["contentDigest","repositoryRelativePath","policyId","policyVersion","detectorId"]`, `retainBody: false` (lines 100–107) — matches RFC5-17's "(content digest, location reference, policy version, redaction class) — never the content itself."

[Observed] PWB-REQ-005 policy-specific fields present: `policyOwningProject: "project:syzygy"` (line 6), `policyVersion: "1.0.0-candidate.3"` (line 4).

**[defect, non-blocking]** RFC5-17's redaction-class vocabulary is closed at three values: `excluded-artifact`, `redacted-span`, `unclassifiable-excluded`. The policy declares only `"redactionClass": "excluded-artifact"` (line 99, inside `matchAction`, which is structurally tied to detector matches) and never emits or names `unclassifiable-excluded` anywhere, even though `sourceAdmission.unclassifiableAction` (line 66) and `classificationOrder` step 5 (line 114) describe a distinct unclassifiable-exclusion path that RFC5-17 gives its own label to. Functionally this is not a fail-open risk — `rawBodyHandling`'s blanket "never" (criterion C above) and RFC5-17's own text ("`excluded-artifact` and `unclassifiable-excluded` withhold the artifact entirely, so every claim that depended on it renders Unknown … `excluded-content`") both apply identically to the unclassifiable path regardless of which of the two labels is used — but the policy as drafted gives an implementer no explicit place to write `unclassifiable-excluded`, so a strict reading of RFC5-17's three-way closed vocabulary is not fully reproduced in this artifact's own field values. File: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`, lines 66, 99, 114. Clause: RFC5-17.

## Criterion D — observer registry entry (RFC4-7 / PWB-REQ-005)

[Observed] PWB-REQ-005 registry-specific fields present: governance home `.syzygy/governance/declarations/adapter-registry` (line 5), project `project:syzygy` (line 6), observed repository `repository:butlers-configured-poc` (line 25), read-only authority described in full (`typedAuthority.readAuthority`, lines 115–116), and an empty write surface (`writeSurface: []`, line 117).

[Observed] All read-only/empty/false fields verified directly: `writeSurface: []`, `databaseAccess: []`, `networkAccess: []`, `executeObservedCode: false`, `workingTreeRead: false` (lines 117–121) — all five are empty/false as required.

[Observed] Both cited digests (`contractVersion` for RFC-0004 general-contract, and `governingBehaviorContract.version` for the PWB spec) are the current accepted/signed ones — see digest cross-checks above.

## Criterion E — no state-(2) or "verified" claim; state (1) explicitly selected with A1 absence explicit

[Observed] None of the three artifacts, `ACT-SEMANTICS.md`, `PWB-EFFECT-ACTS-MANIFEST.txt`, or the generator script claims state (2) or "independently verified" as a present fact. The only occurrences of "independently-verified" are (a) as one of two possible future `authorizationModes` a completed triple of acts could reach (policy line 12, registry line 28), described conditionally ("independently-verified only when all three acts verify through A1," registry line 31) — this is forward-looking evaluation logic, not a claim now; and (b) the consent record's explicit denial, "is never 'independently verified'" (line 68). `ACT-SEMANTICS.md` states plainly: "A record claiming state (2) cannot be produced by this packet" (line 25).

[Observed] State (1) is explicitly the only state these acts can select, and A1 absence is stated as an explicit, non-optional recorded fact rather than a silent omission: "9. A1 audit-record identity | explicitly absent; the act is state (1), `owner-adopted (bootstrap, uncorrelated)`, chosen by performing the phrase; no correlation is claimed" (`ACT-SEMANTICS.md` line 21). This matches RFC3-16(b) item 9's requirement that "omitting the field is invalid; explicit absence is not independent verification" — the field is populated with an explicit absence, not omitted.

[Observed] No artifact's top-level status stamp overclaims: both JSON files declare `"status": "candidate-act-ready-no-effect-until-owner-act"` and the registry entry additionally declares `"adoptionStatus": "candidate-act-ready-unadopted"` (line 164) — status and adoption-status agree, no drift. The consent record's `Status:` line makes the same self-declaration-versus-effective-status distinction RFC3-16 requires ("self-declared stamp; effective status comes only from an owner-act record, RFC3-16," line 22).

[Observed] No artifact claims an act, once performed, is evidence of a read, screening success, or truth. `ACT-SEMANTICS.md`'s closing section states this negatively and explicitly: "None is evidence that a read occurred, that screening succeeded, that admitted content is secret-free, or that any derived claim is true (RFC3-16(c))" (lines 50–51). The consent record repeats the warrant-not-evidence framing at lines 69–71.

## Criterion F — no implementation/body-read/write/egress/execution/deployment/release/recovery/mission/second-repository/autonomous/multi-user authority; nothing reads Butlers

[Observed] `ACT-SEMANTICS.md` lines 52–54 name the full closed list and deny every item on it explicitly: "None grants PWB implementation authority (task 1.8), write, egress, execution, deployment, release, recovery, mission, second-repository, autonomous or multi-user authority." The registry entry's own `implementationStatus` field independently confirms the same for its one implementation-adjacent field: "declared mapping only; no such module exists yet and this entry authorizes no implementation" (line 34) — and the named implementation path `packages/three-surface-poc-core/src/project-shape-observer.ts` was confirmed absent from the working tree (`ls` → no such file).

[Observed] Nothing in the six SUBJECT items reads Butlers. The generator script's every reference to "Butlers" is inside doc-strings, path names of Syzygy-local governance artifacts, or template prose destined for the not-yet-generated `OWNER-SIGNOFF-PACKET.md`/`CANDIDATE-REPORT.md` — it performs no filesystem or network access outside the `ROOT` checkout (`subject_bytes`, `render`, `verify`, `phrases`, `finalized_outputs` all operate only on the three named `.syzygy/**` paths and, for `--finalize`, on `git show`/`git rev-parse` inside the Syzygy checkout itself). No import, subprocess call, or path construction in the script references `/home/tze/GitHub/butlers` or any external repository location; the Butlers repository locator lives only as inert configuration prose inside the (unacted) consent record.

## Criterion G — manifest generator correctness

[Observed] Confirmed directly (see Digest cross-checks): 3-row closed population (`subject_bytes` raises `ValueError` if `len(SUBJECTS) != 3` or the set has duplicates — script lines 60–61), deterministic (`--selftest`'s `first == second` render-twice check passed), and `--selftest`'s output states plainly that byte, digest, path, dropped-row and stray-line mutations are each rejected — read from the printed message, not inferred from exit code alone (exit code was also 0, corroborating). The phrase argument for every act is confirmed to be the artifact's own SHA-256, never the manifest's: `--phrases` output matches direct `sha256sum` of each of the three subject files individually, not the manifest-file digest.

## Criterion H — stale references

[Observed] `grep -rn` across all six SUBJECT files for the superseded PWB spec digest (`07392c11`), the superseded RFC-0004 baseline digest (`2b5072a2`), and the strings `not act-ready` / `not-act-ready` returned zero matches (grep exit code 1, confirming no match rather than a grep failure — command exit was checked, not assumed). No stale reference found in any of the six subject items.

## Prior review's three blockers — still closed in this version

The prior `R-POLARIS-OBSERVATION-GATE-CONFIRMATION-RAW.md` CONFIRMED at different (earlier) digests than this version's (`3c162a72…`/`cfe13100…`/`3e82a4e5…` there, vs `5d705d75…`/`680daf81…`/`d71eadb6…` here — these are later `1.0.0-candidate.3` revisions of the same three artifacts). Re-checked each of its three named fixes against the current bytes:

1. [Observed] "Consent lines 57–61 deny any … body read and deny retroactive authorization; scope prose is now explicitly proposed rather than effective" — current consent record's "Provenance state and effect" section (lines 55–74) still states no effect until act, and the no-retroactive-authorization sentence (lines 73–74) is present verbatim. Still closed.
2. [Observed] "Registry line 88 names a revision-bound manifest validated against the signed PWB grammar, not a separately signed/owner-approved manifest" — this concern's substance now lives in the **policy** file's `sourceAdmission.phaseB.manifestRule`: "manifest must validate against the signed PWB source grammar; it is derived data, not a separate owner-approved artifact" (policy lines 48–50). Still closed; the registry's own `project-shape-source-manifest` input-class entry (registry lines 61–63) is consistent with treating the manifest as derived data with a content-digest identity scheme, not an independently adopted artifact.
3. [Observed] "Registry lines 103–110 split absent versus mismatched/stale/unverifiable authority cases and map absent/unverifiable registry state to RFC4-7's exact `source-uncaptured-or-unreachable`" — current registry's `admissionFailureMapping` (lines 131–138) still splits `missingConsent`/`mismatchedStaleRevokedOrUnattributedConsent`, `missingSecretPolicy`/`mismatchedStaleRevokedOrUnattributedSecretPolicy`, and `missingRegistryEntry`/`mismatchedStaleRevokedOrUnattributedRegistryEntry` into six distinct cases, each still mapped to RFC2-24 reasons (`unconsented-source-or-provider`, `missing-declaration`, `source-uncaptured-or-unreachable`). Still closed.

## Findings summary

| Severity | Criterion | File | Line(s) | Clause |
|---|---|---|---|---|
| defect | C | `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` | 66, 99, 114 | RFC5-17 |
| note | A | `.syzygy/governance/contracts/candidates/pwb-effect-acts/ACT-SEMANTICS.md` (and generator script lines 259, 274) | — | RFC3-16(b) item 3 |

Neither finding is a blocker: neither creates a fail-open path, a false state-(2)/verified claim, an implementation/body-read/write/egress/execution grant, or a stale-digest citation. Both are recommendations for the drafters to tighten before or shortly after the owner acts, not defects that make any of the three offered acts unsafe to offer.

**VERDICT: CONFIRM**
