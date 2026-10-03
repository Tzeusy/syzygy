# Review brief — public-admission registry entries (round 3)

> **Candidate — binds nothing.** This brief says what an independent reviewer
> is given and what they decide. It is not a review and carries no verdict.
> Rounds 1 and 2 returned REVISE; this is the round-3 brief over the repaired bytes.

## What the reviewer is given, and nothing else

CC-REV-1 calls for a fresh context holding only the artifact, its governing
references and the acceptance criteria.

**The artifact under review:** every file of
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, this brief,
`OWNER-DECISION-PACKET.md`, `PUBLIC-ADMISSION-REGISTRY-MANIFEST.txt` and the
two files under `proposed/`), plus
`scripts/build_public_admission_registry_entries.py` and the candidate
registration in `scripts/check_governance.py` (`PUBLIC_REGISTRY_DIR`, `PUBLIC_REGISTRY_MANIFEST`, `PUBLIC_REGISTRY_ACTS`, `_activate_public_registry_manifest_copy_registry`).

**Governing references.**

- RFC4-1, RFC4-2, RFC4-3, RFC4-7 in
  `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`, each
  quoted at its defining clause; RFC3-16(a); RFC5-15 and RFC5-16.
- REQ-polaris-generation-017, 018 and 025 in
  `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`,
  and `openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md`
  ("Required registration fields", "Failure behavior").
- The installed Butlers entry
  `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
  as the shape precedent.
- The egress record at
  `origin/polaris/public-repo-admission:.syzygy/governance/contracts/candidates/public-repo-admission/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`
  (or its merged path), and that package's `OWNER-DECISION-PACKET.md` item 5.
- `decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md` and
  `decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md` (Ceremony).
- `packages/polaris-generation-core/src/pipeline.ts` (`PipelinePorts`).

## Round 2 and the repair

The round-2 raw is `reviews/R-PUBLIC-ADMISSION-REGISTRY-ENTRIES-2-RAW.md`
(REVISE: finding 1 blocking, findings 2 to 10 notes). Repairs, to be checked
against each finding rather than taken on trust:

- F1: the runtime-fixed bytes, the pinned model, empty tools, effort, thinking
  and a max_tokens ceiling are inline in the provider entry (`requestBytes`);
  the acceptance check admits only the generator's parts and `requestBytes`;
  `PROVIDER-EGRESS-BYTES.md` is provenance with a blob and commit named.
- F2: max_tokens and cache_control re-attributed; the pin note is [Inferred].
- F3, F10: the packet's limit list and review statement corrected.
- F4: the packet and delta say accepting O4 needs an egress record version.
- F5: the egress record is to be pinned by digest at the offering.
- F6: scalar determinism explained. F7: per-class RFC2-1 mapping incl. item 11.
- F8: exact fetch string; egress source, acceptance and pinned-field mutants.
- F9: usage reason argued (reason 2); adapter failure, cancellation, deadline.

## Round 1 and the repair

The round-1 raw is `reviews/R-PUBLIC-ADMISSION-REGISTRY-ENTRIES-1-RAW.md` in
this directory (verdict REVISE, 18 findings), retained verbatim. Criterion 12
asks you to check each repair against its finding; do not take the list below
on trust. Population: findings 1 to 18; blocking 1; revise 2 to 9; notes 10 to 18.

- F1, F2: provider entry rewritten around the runtime-fixed bytes (named by
  reference to `PROVIDER-EGRESS-BYTES.md` on PR #258, branch
  agent/dossier-provider; pins SDK 0.3.288 and CLI 2.1.288); acceptance check
  separates envelope from content; unknowns extended.
- F3, F4, F5, F17: failure mappings re-cut (Missing quantity added to the
  builder's set; consent split; non-admitted revision refused before fetch;
  `execution-blocked`).
- F6: per-output-class determinism field. F7: semantics for every limit;
  `maxIndexDepth` removed; oversize blob excluded, never chunked.
- F8: statement that these are not usable entries and what signing buys.
- F9: runtime version and sign-in credential as inputs; model identity as an
  output; credential write unknown. F10: write-surface argument.
- F11 to F16, F18: tool condition and record pin, brief symbols, RFC4-19,
  `--no-tags --no-recurse-submodules`, substitution wording, snapshot mapping note.
- F12: selftest now has a mutant per `REQUIRED` and `ROUTE_KEYS` key, per entry.

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Does each entry carry all seven RFC4-2 declarations?** Walk items 1 to 7
   against each file and quote the field. Name any default left silent.
2. **Does the provider entry equal the egress record's conditions and not
   widen them?** Compare tools, ambient context, telemetry, state location,
   acceptance by captured request and fallback, clause by clause.
3. **Is the write surface honest?** Both `writeSurface` arrays are empty while
   a run directory is written and a network destination is reached. Is the
   split between `writeSurface`, `runDirectoryWrites` and `networkAccess`
   accurate to RFC4-2 item 7 ("the exact write surface, which must be empty
   unless explicitly authorized")?
4. **Is the shallow-by-commit fetch consistent with the observation consent
   scope?** The consent grants the snapshot objects of listed revisions only,
   fetched one commit at a time. Does the entry's `fetch` and `readAuthority`
   match, and refuse more?
5. **Are the determinism classes right?** `capture` for provider replies and
   the fetch; derivation-deterministic transforms over the identified capture.
   Does anything label generated prose Observed?
6. **Are `implementationVersion: null` and the `unknowns` list honest?** Does
   any field state an implementation, version or SDK capability that no
   evidence supports (sweep `apps`, `packages`, `scripts` for a provider SDK
   import; the ledger says 0)?
7. **Are the failure mappings in the RFC2-23 vocabulary, and is the
   uncertain-dispatch mapping defensible?** Test it against the pipeline's
   stop reasons.
8. **Is the signing-path reasoning sound?** Is Scope A correctly judged not
   to cover these entries, and is that labelled Inferred? Is option selection
   at manifest rows the precedent's form?
9. **Is the impact ledger honest?** Re-run Sweeps 1 and 2 and confirm the
   counts and that no reader enumerates the registry directory.
10. **Does the package claim authority it lacks?** No file may label anything
    accepted, adopted, approved or signed off; no Markdown file may carry a
    64-hex digest; `--check` and `--selftest` must pass, and any claim the
    selftest covers with no mutant must be named.
11. **Is each proposed resource limit labelled as a proposal rather than a
    measurement, and does each declared limit have semantics?**
12. **Does each round-1 and round-2 repair hold against its finding, and did any repair
    introduce a new defect?** Re-derive counts and quotes from the bytes.
13. **Does the provider entry's account of the request match
    `PROVIDER-EGRESS-BYTES.md` for the pinned versions, with nothing the
    capture did not show stated as fact?**

## Out of scope

- Whether to perform either act. That is the owner's alone.
- The Agent SDK capability check, the egress and observation consents and
  the public-source screening scope, which are other packages.
- The act recorder, which is written with the acts, against the confirmed
  commit.

## Recording

Store the raw output verbatim in this package's `reviews/` directory as
`R-PUBLIC-ADMISSION-REGISTRY-ENTRIES-3-RAW.md` (a re-issue is a further
`-RAW.md`). **The raw's head is a predicate a recorder will enforce.** The
first four non-blank lines must be the title and exactly:

```text
Reviewed commit: <the 40-hex commit the reviewer read>
Manifest SHA-256: <SHA-256 of the FILE PUBLIC-ADMISSION-REGISTRY-MANIFEST.txt>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of the manifest **file**, which carries both
entries' arguments as rows; it is not either row. Print it with
`python3 scripts/build_public_admission_registry_entries.py --manifest-digest`.
Keep the verdict inside the first four non-blank lines. Number findings
`**Finding N — title** (blocking|revise|note)` under `## Findings`. A CONFIRM
WITH EXCEPTIONS clears the bytes only when every finding is a `note`,
dispositioned in a sibling `ROUND-<n>-DISPOSITIONS.md` naming the raw on a
`Reviewed record:` line. Any later edit retires the review (rule 10).
