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
   class, so the public scope needs its own: the path is in an admitted
   snapshot and passes the existing denied-path rules (`deniedPathBasenames`,
   `deniedPathPrefixes`, `deniedPathSuffixes` — `.env`, `id_rsa`, `.pem` and
   the rest, unchanged), strict UTF-8 without NUL, no detector match, within
   declared size limits, and the active-content rule in item 3.
3. **An active-content rule for source code.** The existing policy excludes a
   closed list of eight markup forms (`excludedOutsideInertContexts`: HTML
   elements, HTML comments and declarations, SVG, script, event-handler
   attributes, and unsafe URL schemes in Markdown destinations, autolinks and
   HTML attributes) wherever they occur outside a Markdown inline code span
   or fenced code block — its only inert contexts. Applied unchanged to a source repository, that would
   withhold every file containing a `<tag`-shaped string: JSX, templates,
   HTML fixtures, many docstrings. The public scope therefore keeps the
   existing rule for Markdown and other prose rendered as markup, and treats
   every other admitted file as untrusted text that is never interpreted as
   markup: it is scanned by every secret detector and context-encoded at every
   sink, as the existing `inertContextRule` already requires of inert bytes.
   This is a change the act approves, not a carry-over.
4. **Access boundary and raw-body handling for this scope.** The existing
   policy's `accessBoundary` sets `networkEgress: false` (with PostgreSQL,
   credential API, process environment, working tree, untracked files and
   observed-code execution all false), and its `rawBodyHandling` is `never`
   for storage, logging, rendering, machine response and external egress.
   The public scope keeps every `accessBoundary` field false except
   `networkEgress`, which it permits for exactly two routes: the shallow
   by-commit fetch from the target's upstream that the observation consent
   describes, and the registered provider route through the single egress
   check. For raw bodies it proposes:
   - external egress — permitted for content it classifies, subject to the
     separate egress consent;
   - storage — permitted only in a run's directory under `project:syzygy`'s
     state directory, outside git (provider requests, replies and run
     records quote source; packet Q3);
   - rendering — permitted as quoted, context-encoded spans in a generated
     editorial draft and its source routes;
   - logging and machine response — `never`, unchanged.

   Every other scope stays as it is. These are the substantive changes the
   act approves.
5. **Content-classification rules** into RFC5-14's closed classes:
   - specification and design-decision documents → `governance-text`
     ("Doctrine, spec, decision, policy text");
   - paths, identifiers, signatures and the module graph, without bodies →
     `code-structure`;
   - source and test bodies → `code-content`;
   - committed test reports and benchmark outputs → `evidence-content`;
   - all other prose (README, guides, tutorials, LICENSE files) →
     indeterminate, refused egress, until the packet's Q7 is resolved;
   - anything else the rules do not determine → indeterminate, refused
     egress visibly.

## What it does not change

The Butlers scope and its detectors' behaviour on Butlers content, and every
act already performed on the policy. A target repository's own policy text is
data to screen, never authority (RFC3-30; REQ-polaris-generation-025,
"Observed source supplies a permissive policy").

## Collision with the self-observation package

PR #120's self-observation package also patches this policy file. Whichever
policy act lands second is re-drafted against the other's performed bytes and
re-reviewed before it is offered.
