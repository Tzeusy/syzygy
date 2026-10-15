# Candidate CAP1 consent design and plan amendment

> Non-effective design. This is a medium-sized security/interface change to one
> existing capability, not an additional service or implementation permission.

## Baseline and placement

[Observed] CAP1 core owns pure consent resolution; cap1-daemon loads exact consent
references and gathers repository inputs; app and machine routes expose the same
ProjectEvaluation. Existing consent.ts/consent-loading.ts carry record facts but
not the proposed complete effective-act admission. The held runtime-hardening
plan names capture/consent as Task 1, coverage as Task 5 and discoverability as
Task 6. These boundaries remain; their old provider-only assumptions do not.

[Inferred] One daemon-boundary admission operation returns an immutable consent
decision to capture. Core models describe facts and results; I/O and owner-act
record loading remain daemon responsibilities. Coverage, explanations and both
serializers consume that decision and cannot independently regrant consent.
No new package, service, third-party dependency or scheduler is proposed.

## Record and decision contract

Reference RFC3-16(b)'s nine binding items; do not redefine its owner-act model.
The act record references a distinct consent artifact digest, avoiding a digest
that hashes itself. The exact owner phrase, act record and recording commit/tag
remain the state-(1) evidence chain under RFC3-16(c). Binding includes the exact
project/repository observation scope and consent/revoke act type.

Replace the old mandatory-audit OwnerActBinding projection with a common binding
plus an explicit provenance sum: state (1) carries absent A1 identity; state (2)
carries the audit identity and correlation evidence. Missing fields are never
filled from defaults. Do not reuse the old name VerifiedConsentRecord for both
states: the closed result distinguishes effective-bootstrap, effective-correlated
and refused, carrying identity/digest, source references, evaluation/as-of and
reason. Exact serialized spelling/version must be reviewed before implementation;
no new on-disk schema is adopted by this sketch.

A real human must perform each act. The operator-controlled recording workflow
prepares exact bytes for attendance and records the performed scope; an API caller
flag, stored owner name or fixture does not establish attendance. There is no
cryptographic forgery-proof promise for state (1): its admitted trust premise is
explicit trust in the owner's tree. Recognized non-human acts are refused; an
undetectable forgery remains unauthorized rather than becoming a valid act.

## Capture and read ordering

1. The already-authorized observation input boundary admits only the declaration,
   referenced consent artifact and its act evidence necessary to decide scope.
   This proposal grants no otherwise-forbidden metadata/body read; unsupported
   authority-source acquisition is a stop, never a reason to pre-read the repo.
2. Capture those exact bytes and evaluate the bindings at the explicit as-of.
   State (1) is permitted only when explicitly selected in the actual act. State
   (2) invokes the existing injectable correlation boundary; absent provider or
   indeterminate result refuses that state without fallback.
3. Retain grant and withdrawal evidence. A valid withdrawal wins; unreadable or
   invalid referenced withdrawal refuses the pair, rather than dropping a denial
   signal. Ambiguous competing acts refuse until owner resolution.
4. Only an effective, in-scope grant admits dependent content reads. Capture the
   decision, its authority inputs and admitted content into the existing immutable
   snapshot design. All later evaluation/serialization uses this capture.

No post-capture filesystem lookup, network retry, last-good fallback or implicit
act upgrade is permitted. Content read/parse failure after admission remains the
existing coverage failure, not a withdrawal or a claim that content was observed.
Repeated identical inputs/as-of yield identical decisions; a changed input or
later correlation is a new snapshot/evaluation. Failed capture serves its honest
existing failure rather than a partial successful snapshot.

## Human and machine presentation

[Inferred] Use the existing coverage and Why-this-answer paths. Show consent
status, then plain provenance: owner-adopted (bootstrap, uncorrelated) or
Syzygy-verified. Explain that permission is not execution success. Put exact act,
artifact and evaluation references in the existing disclosure, keyboard reachable
and non-visually readable. Both channels expose the same tuple. An absent or
invalid act renders Unknown with the existing primary reason plus its specific
diagnostic and owner resolution route. Do not invent a score or an extra approval
screen. This follows CAP1-REQ-040/041/045/064 and the design bar's accessible,
consistent, low-friction presentation bias.

## Compatibility, retention and rollback

Legacy consent records without a complete explicit act do not auto-upgrade and
cannot authorize observation through the amended path. They remain visible as
recorded facts with authorization Unknown. No rewrite, migration, provider-store,
credential custody, audit retention rule or extra history store is introduced.
Snapshot ownership remains with the existing capture slice. Sensitive content
never enters consent diagnostics; retain identities/digests and safe reasons.

Before adoption, remove only the new candidate as a unit if declined. After
adoption, reversal of the normative change requires a new owner-governed reverse
delta. The old files and acts remain historical evidence; code rollback does not
revoke an owner act and must preserve refusal for unsupported authority states.

## Alternatives

The owner selected bootstrap proposal preparation over designing a new independent
local audit service, identifying an existing provider, or keeping the provider-only
planning route. The operational hold remains while this successor is reviewed.
A service has stronger independently correlated provenance but extra administration
and retention obligations. It can be proposed separately; there is no silent
fallback from that route to bootstrap. No owner-held key design is proposed.
