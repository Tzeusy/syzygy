# Polaris precondition read-boundary incident

Date: 2026-08-31

Governing requirement: `polaris-project-wide-butlers-model/PWB-REQ-005`

## What happened

[Observed] After the project-wide specification was signed and the owner gave
plain-language observation consent, the primary agent used `rg` against these
Butlers documentation bodies while checking the owner's PostgreSQL statement:

- Butlers path *docs/identity_and_secrets/environment-variables.md*
- Butlers path *docs/identity_and_secrets/owner-identity.md*

[Inferred from the audit agent's report] A parallel implementation audit then
read these exact Git blobs:

- Butlers path *about/README.md*
- Butlers path *about/heart-and-soul/README.md*
- Butlers path *about/heart-and-soul/vision.md*
- Butlers path *about/heart-and-soul/v1.md*
- Butlers path *about/legends-and-lore/README.md*
- Butlers path *about/lay-and-land/README.md*
- Butlers path *about/lay-and-land/components.md*
- Butlers path *about/craft-and-care/README.md*

The audit also reported running one Markdown-wide search. [Unknown] The exact
population of bodies opened by that search was not retained.

The agents treated direct owner consent as sufficient before reconciling it
with PWB-REQ-005's separate policy, registry and independently verified
provenance requirements. That was wrong: PWB-REQ-005 required zero body reads
until the complete triple verified.

## Impact and containment

[Observed] No project-wide body-derived fact was admitted into the running POC
model. The primary-agent command printed only the named documentation matches.
[Inferred from the audit agent's report] The audit performed no PostgreSQL,
credential API, environment-file, implementation-body, network, execution or
write access and printed no secret-like value.

The audit was stopped as soon as the mismatch was identified. Its reported
project denominator is inadmissible as runtime evidence and will not seed an
implementation fixture or a positive Polaris claim. No further Butlers body
read is permitted while PWB-REQ-005 remains unsatisfied.

## Follow-up

- Preserve the owner's consent statement without calling it independently
  verified.
- Keep the secret policy and adapter-registry entry as non-effective
  candidates until owner and provenance gates are resolved.
- Test the eventual authority verifier with a read spy so every invalid triple
  proves zero body calls before any live demonstration.
