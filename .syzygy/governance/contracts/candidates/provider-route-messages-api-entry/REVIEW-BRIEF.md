# Review brief — Messages API provider route registry entry (round 1)

> **Candidate — binds nothing.** This brief says what an independent reviewer
> is given and what they decide. It is not a review and carries no verdict.

## What the reviewer is given, and nothing else

CC-REV-1 calls for a fresh context holding only the artifact, its governing
references and the acceptance criteria.

**The artifact under review:** every file of
`.syzygy/governance/contracts/candidates/provider-route-messages-api-entry/`
(`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, this brief,
`OWNER-DECISION-PACKET.md`, `MESSAGES-API-ROUTE-REGISTRY-MANIFEST.txt` and the
file under `proposed/`), plus
`scripts/build_provider_route_messages_api_entry.py` and the candidate
registration in `scripts/check_governance.py` (`MESSAGES_API_DIR`,
`MESSAGES_API_MANIFEST`, `MESSAGES_API_ACTS`,
`_activate_messages_api_manifest_copy_registry`).

**Governing references.**

- RFC4-1, RFC4-2, RFC4-3, RFC4-7 in
  `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`, each
  quoted at its defining clause; RFC2-23, RFC2-24; RFC3-16(a); RFC5-15, 16.
- REQ-polaris-generation-017 in
  `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
  and `openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md`.
- The installed Butlers entry
  `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
  as the shape precedent.
- PR #255 (the Agent SDK provider entry this one substitutes; its proposed
  file and OWNER-DECISION-PACKET.md) and PR #215 (the confirmed Anthropic
  egress record, EGRESS-CONSENT-ANTHROPIC.md).
- PR #264: the route's source (the adapter, its request builder and the
  runtime egress gate), at the commit and blobs the entry's `provenance`
  fields name. **No review record of #264's header list exists; re-derive the
  header list and `requestBytes` from that source and the installed SDK
  0.131.0 rather than taking the entry's list on trust.**

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Does the entry carry all seven RFC4-2 declarations?** Walk items 1 to 7
   and quote each field. Name any default left silent.
2. **Is it a substitute and nothing more?** Same subject and authority type as
   PR #255's entry; RFC4-1 satisfied by exactly one being adoptable; the
   `routeSubstitution` block says so and the packet does not suggest both.
3. **Does `requestBytes` equal what the route sends?** Re-derive the headers,
   body fields and endpoint from PR #264's source and SDK 0.131.0. Is any sent
   byte unlisted, or any listed byte not sent (for example `x-stainless-timeout`,
   `accept-language`, `sec-fetch-mode`)? Is anything the route does not send
   claimed as fact?
4. **Is the egress record fit honest?** Compare the entry's `egressRecordFit`
   with PR #215's record clause by clause. Does the entry claim "no new egress
   version" anywhere it should not? The packet and delta say it depends on the
   owner's reading of three wordings; is that accurate?
5. **Is the credential handling honest?** API key only; one named environment
   variable; never logged. Is the name labelled a proposal? Does anything in
   PR #264's source log or persist the key?
6. **Does the runtime egress gate description match PR #264's source?** The
   three forwarding rules, the 403 refusal and the provenance by commit and
   blob.
7. **Are the pinned profile fields right and labelled?** Model, effort, tools
   absent, thinking off or adaptive with `budget_tokens` refused, and the
   64000 ceiling as an [Inferred] proposal.
8. **Is the write surface honest?** `writeSurface` empty; state any run-
   directory write or network destination under the right field (RFC4-2 item 7).
9. **Are `implementationVersion: null`, the `unknowns` list and the failure
   mappings honest and in the RFC2-23 and RFC2-24 vocabularies?** Does any
   field state an implementation or capability no evidence supports?
10. **Is the impact ledger honest?** Re-run Sweeps 1 and 2 and confirm counts.
11. **Does the package claim authority it lacks?** No file may label anything
    accepted, adopted, approved or signed off; no Markdown file may carry a
    64-hex digest; `--check` and `--selftest` must pass, and any claim the
    selftest covers with no mutant must be named.

## Out of scope

- Whether to perform the act, or which route to choose. That is the owner's.
- The egress and observation consents and PR #255's source-acquisition entry.
- The act recorder, which is written with the act, against the confirmed commit.

## Recording

Store the raw output verbatim in this package's `reviews/` directory as
`R-PROVIDER-ROUTE-MESSAGES-API-ENTRY-1-RAW.md` (a re-issue is a further
`-RAW.md`). **The raw's head is a predicate a recorder will enforce.** The
first four non-blank lines must be the title and exactly:

```text
Reviewed commit: <the 40-hex commit the reviewer read>
Manifest SHA-256: <SHA-256 of the FILE MESSAGES-API-ROUTE-REGISTRY-MANIFEST.txt>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of the manifest **file**, not its row. Print
it with `python3 scripts/build_provider_route_messages_api_entry.py
--manifest-digest`. Keep the verdict inside the first four non-blank lines. Number
findings `**Finding N — title** (blocking|revise|note)` under `## Findings`. A
CONFIRM WITH EXCEPTIONS clears the bytes only when every finding is a `note`,
dispositioned in a sibling `ROUND-<n>-DISPOSITIONS.md` naming the raw on a
`Reviewed record:` line. Any later edit retires the review (rule 10).
