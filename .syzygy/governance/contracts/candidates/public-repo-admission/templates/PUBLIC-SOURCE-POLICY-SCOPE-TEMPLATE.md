# Public-source screening scope — outline

> Outline, not a filled record. Candidate — binds nothing. The filled form is
> a versioned extension of the observing project's secret-classification
> policy, drafted against that policy's then-current bytes, with its own act.

## What the extension adds

1. **A scope for public repositories.** The same secret detectors and
   exclusion rules as the existing policy, applied to every admitted public
   target. Public visibility does not exempt content: a committed credential is
   excluded with hash-not-body provenance (RFC5-17) exactly as anywhere else.
2. **Content-classification rules** that map concrete content into RFC5-14's
   classes, so the egress check can decide:
   - prose documentation, specifications, RFC-like design docs, licences →
     `governance-text`;
   - paths, identifiers, signatures, the import and module graph, without
     bodies → `code-structure`;
   - source and test bodies → `code-content`;
   - test reports and benchmark outputs committed to the tree →
     `evidence-content`;
   - anything the rules do not determine → indeterminate, which refuses
     egress visibly.
3. **Active-content handling.** Executable configuration (install scripts,
   CI workflows, build files) may be read as text, is never executed, and is
   classified `code-content`.

## What it does not change

The Butlers scope, its detectors' behaviour on Butlers content, and every act
already performed on the policy. A target repository's own policy text is data
to screen, never authority (REQ-polaris-generation-025, "Observed source
supplies a permissive policy").
