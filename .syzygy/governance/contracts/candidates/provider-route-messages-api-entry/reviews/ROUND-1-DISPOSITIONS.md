> **Candidate — binds nothing.** Dispositions of the round-1 findings on this
> package. It is not a review, carries no verdict and confirms nothing; a
> later round decides whether each disposition is true of the bytes it names.

# Round-1 dispositions — Messages API provider route registry entry

Reviewed record: .syzygy/governance/contracts/candidates/provider-route-messages-api-entry/reviews/R-PROVIDER-ROUTE-MESSAGES-API-ENTRY-1-RAW.md

Revise-severity findings: 5

The raw's verdict of record is REVISE (findings 1 to 5 revise, 6 to 13 note
in the raw's numbering: Finding 1 to 5 and Note 1 to 8). It read commit
b101829d1b6f345a166e8eeed8efb4e800544421, whose adapter source is the PR #264
commit dd526b0c. The raw is retained verbatim and not edited; this round's
repairs retire its confirmation (rule 10). The entry is now pinned to the
later PR #264 commit e76b6929, which the round-1 reviewer did not read; the
reviewer's observations about SDK 0.131.0 and the capture still hold of the
library, and each is re-checked below against that commit where it concerns
the adapter.

**Finding 1 — x-stainless-timeout (revise).** Repaired. The header is the
literal 600 in `headers.pinnedLiterals`, no longer a value rule, with a
`timeoutNote` saying the SDK always sends it and that an implementation must
enforce the literal because the cited predicate checks the name only. The
builder compares the whole literal table by value.

**Finding 2 — SDK environment inputs (revise).** Repaired. The entry declares
`typedAuthority.sdkEnvironmentInputs`: ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN,
ANTHROPIC_CUSTOM_HEADERS, ANTHROPIC_LOG, ANTHROPIC_BASE_URL and any other
ANTHROPIC_-prefixed variable, each with its effect and a fail-closed posture
(unset), the client constructor arguments, and a new input class
`sdk-environment-variables` with its snapshot mapping. The retention line is
stated as satisfied only while ANTHROPIC_LOG is unset. On the enforcement
point: [Observed] the adapter at the pinned commit e76b6929 throws
`ambient-environment` when any ANTHROPIC_-prefixed variable is set; at dd526b0c,
which the reviewer read, it did not. The entry says both and labels the
enforcement [Inferred] pending the offering's re-check; it does not rest on
the guard alone, because the postures are the entry's own statement.

**Finding 3 — the destination (revise).** Repaired. `networkAccess` names
https://api.anthropic.com/v1/messages, POST only, and a gate rule requires the
configured upstream to equal that origin. [Observed] the gate at the cited
commit accepts any upstream URL including plain http, so the rule is the
entry's statement and is on PR #258's fix list [Inferred]; the entry says it
is not present at the cited commit.

**Finding 4 — two versus three wordings (revise).** Repaired. The conclusion
says three wordings, the builder checks that the number in the conclusion
equals the length of `needsReading`, and the delta and packet already said
three.

**Finding 5 — the role identity (revise).** Repaired by the first of the
reviewer's two routes. RFC4-9 is quoted whole in the entry and the delta; the
entry carries PR #255's role identity (`observerId`) and registers a new
implementation identity, so RFC4-1's one-adapter rule is held by the registry
shape and not by a prose flag alone. The entry says what retires the other
entry in either order of adoption. [Inferred] The shared role name spells the
Agent SDK for historical reasons; renaming it belongs to PR #255's entry.

**Note 1 — Node fetch headers.** Accepted. `accept-language`, `sec-fetch-mode`
and `accept-encoding` are attributed to Node's built-in fetch in
`runtimeFixed`, Node is stated as not pinned, and `runtimePin.note` says the
literals also depend on Node. The packet's O2 reading ("fixed by the
runtime") now has these three headers as the bytes a runtime fixes.

**Note 2 — thinking and model pins.** Accepted without change: the entry
already says the adapter accepts the budget form and the entry refuses it, and
a later offering must show the refusal in code.

**Note 3 — contractVersion.** Accepted as disclosed: the value is inherited
from the Butlers entry, its source is labelled and the entry says to re-derive
it before the offering. No change here; the re-derivation will differ.

**Note 4 — gate decision records.** Accepted. The wording "name fields, never
values" is replaced: the records are free of the credential and the body and
carry the method, the URL path and header names.

**Note 5 — uncovered claims.** Accepted. The selftest now has a mutant for
every header literal (drifted and dropped), the timeout literal, the
conclusion and needsReading agreement, the network destination (no scheme,
http, another host), the upstream rule, every SDK environment input and its
posture, the role-identity and implementation-identity rules, and a sibling
cross-check that also compares contractVersion and implementationId; 190
predicates held. The provenance blobs were already checked against git when
the commit is present.

**Note 6 — SDK file-write Unknown.** Accepted, kept as an Unknown. The
reviewer's source locations are noted; narrowing it needs the isolation test
to cover file writes.

**Note 7 — the act phrase.** Accepted. The packet names the registered phrase
and says it matters only for the typed-phrase form, with the same row as its
argument; the recorder and the act state which form binds.

**Note 8 — O1 to O4.** Left as the owner's choices, as the reviewer says.
