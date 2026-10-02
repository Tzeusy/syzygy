# Public-source screening scope — outline

> Outline, not a filled record. Candidate — binds nothing. The filled form is
> a versioned extension of `project:syzygy`'s secret-classification policy,
> drafted against that policy's then-current bytes, with its own act.

## What the extension adds

1. **A scope for admitted public repositories.** The existing secret
   detectors apply unchanged. Public visibility exempts nothing: a committed
   credential is excluded with hash-not-body provenance (RFC5-17) exactly as
   anywhere else.
2. **Its own classification-success rule.** The existing rule admits a body
   only when "its extraction class is in the signed PWB closed set"; source
   code and documentation of an arbitrary repository have no PWB extraction
   class, so the public scope needs its own: strict UTF-8 without NUL, no
   detector match, no active-content form outside an inert context, within
   declared size limits.
3. **Active content withheld, as today.** The existing policy withholds
   active content (executable configuration such as TOML, CI workflows and
   build files outside an inert context). The public scope keeps that rule;
   such files are counted as withheld, never read into a prompt.
4. **Egress for this scope only.** The existing policy states
   `"externalEgress": "never"`. The public scope permits egress of content it
   classifies, subject to the separate egress consent; every other scope
   stays `never`. This is the substantive change the act approves.
5. **Content-classification rules** into RFC5-14's closed classes:
   - specification and design-decision documents → `governance-text`
     ("Doctrine, spec, decision, policy text");
   - paths, identifiers, signatures and the module graph, without bodies →
     `code-structure`;
   - source and test bodies → `code-content`;
   - committed test reports and benchmark outputs → `evidence-content`;
   - all other prose (README, guides, tutorials) → indeterminate, refused
     egress, until the packet's Q7 is resolved;
   - anything else the rules do not determine → indeterminate, refused
     egress visibly.

## What it does not change

The Butlers scope and its detectors' behaviour on Butlers content, and every
act already performed on the policy. A target repository's own policy text is
data to screen, never authority (RFC3-30; REQ-polaris-generation-025,
"Observed source supplies a permissive policy").
