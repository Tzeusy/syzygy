# The owner's RFC7-20 reading for operator-agent runs — exact-bytes record

> Template. Replace every `{{…}}` field; a filled record with any `{{` left is
> invalid. Candidate — binds nothing until the owner acts on the filled record.
> The bound-files table is computed from the file's current bytes.

Date: {{DRAFT_DATE}} (drafted); the act, if performed, records its own instant

Owner: {{OWNER}}

Record ID: `RFC7-20-READING-IN-FORCE-OPERATOR-AGENT`

Record version: `{{VERSION}}`

Record class: in-force record for a plain owner direction (RFC3-16(a); the
review note R3-F8 of the local-agent mode)

Subject: item 1 of the owner direction `{{DIRECTION_ID}}`, and only item 1

Direction: {{DIRECTION}}

Bound file (whole-file SHA-256, computed when this record was generated):

{{BOUND_FILES}}

Proposed provenance state: `owner-adopted (bootstrap, uncorrelated)` —
state (1), RFC3-16; A1 audit-record identity explicitly absent

Proposed revocation state: active; supersedes no earlier record

## What it decides

Item 1 is the owner's reading of RFC7-20: the condition "absent SEC-2
named-provider consent it is not computed" governs drafts that Syzygy
computes. A draft the operator's own agent session computed is admitted to
the draft layer, as an editorial draft, only when the run record and every
page disclose how it was computed, the operator has declared the agent tool
and provider and Syzygy has recorded them, and every rendered quotation is
byte-verified against the pinned blobs. REQ-polaris-generation-033 applies
that reading, and the review note R3-F8 requires the reading to be
established by the act cross-check before Syzygy relies on it.

Scope: Syzygy may treat item 1 as in force for REQ-polaris-generation-033's
draft-layer rule while the file hashes to the digest above. For any other
bytes, or with this record withdrawn, the reading is not established, and an
operator-computed draft layer renders Unknown (`unconsented-source-or-provider`)
in both channels while the source pages and disclosures stay readable.

## What it does not do

It does not establish item 2 of the same direction (code execution by the
agent); D9 and its own record govern that. It does not amend RFC7-20 or any
contract, and it governs no draft that Syzygy computes or dispatches. The
owner chose this reading knowing that a reviewer may call it a contract
change; this record preserves that trade-off and does not resolve it.

## Cost

The digest is of the whole direction file. Any later edit to it leaves the
reading unestablished until a new version of this record is generated and
acted on.

## Withdrawal

Withdrawal is a later owner act naming this record; it is prospective.
