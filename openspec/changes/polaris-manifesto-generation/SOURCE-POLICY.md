# Source admission, classification and exclusions — candidate

Proposed detail for REQ-polaris-generation-025, supplementing existing admission,
adapter, audit and revocation requirements. It grants no new read, write, provider
or execution consent and changes no adopted project's screening policy.

## Resolve the actual authority and consent records

The observing project and its governance root come from the owning declarations;
they are not inferred from the generated page's label or an observed repository's
directory. Observation/write consent is per repository. Egress consent is one
record per project/provider pair naming permitted content classes. Execution
consent is per project for an exact approved execution-profile version. Each
record grants exactly one consent class and records its subject, scope, granting
principal, grant instant and revocation state. Those classes remain separately
revocable and visible; permission to read never implies permission to send,
write or run observed code.

Adapter registration, classification-policy approval, secret-policy approval and
consent are separate authority checks. A genuine consent record does not make an
unapproved permissive policy effective. A policy's approval warrants its use,
not the truth of a generated claim or success of a transmission or screening.

## Carry content provenance through composition

The egress vocabulary remains governance-text, code-structure, code-content,
work-history, evidence-content and derived-composites. The effective declared
classification policy classifies concrete content and determines the composite's
inherited highest embedded class from its actual input provenance. Composing a
prompt, summary or embedding carries embedded classifications and origins forward;
the composer's self-assigned output label cannot replace that derivation.

No total order is invented from the vocabulary's printed or lexical order, and
this contract does not introduce a separate requirement that every embedded
class appear independently in consent. The approved policy must make the
inherited classification determinable. Where its rules or input provenance do
not determine it, refuse egress and show the refusal. Derived-composites consent
alone never launders otherwise unconsented content. Classification results and
policy versions stay auditable and identity-bound to the snapshot.

Every network transmission of governed-project content crosses the single egress
check, including side effects and remote backing dependencies. At the actual
effect boundary it verifies the in-force project/provider consent, determinable
permitted classification under an effectively adopted policy, and the consent's
own effective act. Both acts' exact provenance states are disclosed. An invalid
purported consent act refuses transmission and produces the prescribed
Contradiction; mere absence is not fabricated into a purported act. None of these
checks can be supplied by a provider response or registration label.

## Screen at every ingest, under the observer's policy

Before content enters any store, surface or endpoint, apply the observing
project's effectively approved secret-detection policy bound to its exact digest.
This includes source acquisition, cross-project reads, workspace imports,
provider responses, evidence, adapter results, telemetry and diagnostic metadata;
the examples are not an exemption list. The observed project's policy text is
data to screen, not authority to replace the observer's policy.

The policy version is a snapshot input and its exact act provenance is visible.
Missing or invalid policy authority blocks ingestion. Secret matches and content
that cannot be classified are excluded, not indexed pending a later review.
Approval of the detector is never displayed as proof that the content contains
no secrets. No content field or newly introduced route bypasses the boundary.

## Preserve useful surviving evidence

Exclusion provenance records content digest, location reference, policy version
and one of the existing redaction classes. Excluded bytes never enter the record,
audit or any other store. Location metadata is also subject to screening; an
opaque permitted reference can locate an exclusion without exposing an excluded
path string.

| Redaction class | Observable result |
|---|---|
| excluded-artifact | Withhold the artifact; every dependent claim is Unknown with excluded-content and the exclusion count. |
| unclassifiable-excluded | Withhold the unclassifiable artifact under the same Unknown/count rule; this is the fail-closed default. |
| redacted-span | Retain permitted surviving content and counted markers. Claims supported by surviving content keep their otherwise-earned tier and disclose the redaction count; only claims depending on removed spans become Unknown with excluded-content. |

This table defines branch semantics, not permission to choose a more permissive
branch. If an adopted project policy permits only whole-artifact exclusion, the
generator cannot introduce partial redaction. Its source/claim support mapping
must be sufficient to distinguish surviving support from removed support; missing
classification/support information cannot be repaired by guessing.

## Revocation does not rewrite challenge history

The immediate enforcement, withdrawal label and forced evaluation in REQ-022
remain the common mechanism. A revoked provider's overlays are not recomputed
and admit no new kernel challenges. Already-admitted challenges keep their
lifecycle and leave only through their governing resolution act; revocation
neither silently resolves nor unsuspends them. Historical records remain with
withdrawal visible. This concerns the kernel Challenge lifecycle, not a ban on
the owner reporting a problem or drafting a repair.

Existing Butlers admission and screening rules remain controlling. A new generic
schema, an available source file or a useful README finding cannot broaden its
consented population or relax its literal grammar. Any needed policy/registry
change is a separately reviewed and authorized change, not generator fallback.
