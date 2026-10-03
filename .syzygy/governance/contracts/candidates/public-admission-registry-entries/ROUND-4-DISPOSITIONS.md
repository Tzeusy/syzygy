> # Record beside the package — not authority, binds nothing
>
> Dispositions the notes of the round-4 fresh confirmation review of the
> public-admission registry entries. It is not a package artifact: the
> manifest does not hash it and no builder reads it. Nothing here offers a
> phrase or performs an act (VIS-4).

# Round 4 dispositions — public-admission registry entries

- **Reviewed commit:** `d08f4400cd20a9babc38e30b5fa6197b696e96e2`.
- **Raw:** `reviews/R-PUBLIC-ADMISSION-REGISTRY-ENTRIES-4-RAW.md`, retained
  verbatim (CC-REV-6).
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`; five notes, no revise or
  blocking finding.
- **Effect:** under the owner ruling of 2026-09-26 a notes-only round clears the
  bytes it read. No package byte is edited by this record. Where a note names a
  sentence in the confirmed bytes that is wrong, this record states the
  correction, and the owner sitting presents the corrected statement.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-admission-registry-entries/reviews/R-PUBLIC-ADMISSION-REGISTRY-ENTRIES-4-RAW.md
Revise-severity findings: 0

Arguments the reviewed manifest carries, copied by script (`--digests`); each
goes stale the moment its entry moves, which is rule 10 made visible:

ADOPT POLARIS PROVIDER EXECUTION ROUTE REGISTRY ENTRY: 3e544fbdc623544d62dd718d227926b9c8b4366087df5842c89b3a874a099395
ADOPT POLARIS PUBLIC GIT SOURCE-ACQUISITION REGISTRY ENTRY: e50036e266f5147b95ec5a5d9f466c9068033aa357f46486e670f775c5483240

## Dispositions

### 1 — "the cited gate has a stripFingerprint option": the cited gate has none

**Correction, stated plainly: the sentence in the confirmed provider entry
(requestBytes.headers.machineFingerprint) and the matching sentence in the
packet's O4 are wrong about the cited gate.** The gate blob the entry cites
(the one at commit 3444c33f) offers only `upstream` and `permitted`. A
`stripFingerprint` option, default off, first appears in a later commit of the
same branch (abc9d411, "optional fingerprint strip in the gate"), where the gate
is a different blob. The entry's boundary is unaffected: the three
machine-identifying headers are in its closed set and stated as sent, and the
strip choice is the owner's with no answer assumed. Left in the confirmed
bytes. The owner sitting presents the strip as an option of a later gate
version, not of the cited one, and a usable (later) entry version carries the
corrected sentence and a provenance pair that contains the option.

### 2 — the packet's review sentence is stale

Left. The packet says rounds 1 and 2 returned REVISE; round 3 also did, and
round 4 returned this verdict. The delta and brief already say so; the
packet's sentence is superseded by this record.

### 3 — three header-table rows differ from the cited predicate

Left; none widens the boundary the entry binds. (a) `connection` is the one
header whose value rule is a token class, not a literal or a shape; the cited
gate deletes `connection` before forwarding and the transport sets its own. (b)
The second half of the `host` rule and the machine-fingerprint sentence come
from the gate's forwarding code, not from the acceptance predicate the builder
comment says the table was copied from. (c) The entry binds only the endpoint
with the query string; the cited predicate also accepts the bare path, so a
later implementation narrows to the entry. A usable entry version states each
of these exactly.

### 4 — "signed in with the owner's account" cannot pass the closed set

**Correction: under these bytes Route A is API-key only.** The closed header
set carries `x-api-key` and no `authorization` header, and the cited adapter
requires an API key. An account (OAuth) sign-in would carry a bearer credential
outside the set and fail the acceptance check, so the entry's "account or key"
wording and O3's treatment of a subscription login as open are superseded:
that login cannot pass. It fails closed, so no effect is widened. The owner
sitting states that Route A needs an API key and that an account login would
need a further entry version, and it weighs that against Route B, which also
needs a key.

### 5 — selftest residuals

Left; the claims the selftest covers with no mutant are named by the raw
(appended text in `runtimeFixed`, `generatorBuilt`, `bodyFields`, `endpoint`,
`probe`, `egressGate`, `ambientContext`; prefix and substring tests on
`thinking` and `maxTokensCeiling`; a prepended clause in `acceptanceCheck`; the
git provenance re-check returning nothing when the commit is absent). A usable
entry version closes them with exact-value checks.
