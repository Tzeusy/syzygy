## Why

The owner-led cold-open walkthrough found that Polaris does not explain
Butlers. It presents one WhatsApp capability as the whole surface, and its
meta-language makes a thin model harder to read.

This change makes project-wide comprehension and complete declared-shape
coverage explicit POC evaluation criteria.

## What Changes

- Polaris opens with a concise project account: purpose, promises, non-goals,
  architecture, V1 scope and success criteria.
- The shared model accounts for every declared staffer, domain butler, module,
  connector and major interface in the configured Butlers revision.
- Coverage reports a complete denominator. Missing or unreadable declarations
  remain visible as Unknown; they never disappear from the count.
- Capability material becomes drill-down content beneath the project account.
  The existing WhatsApp slice remains a proving example, not the definition of
  Butlers.
- Active and proposed OpenSpec work appears only within the affected
  capability's drill-down; it does not dominate the project-level narrative.
- Polaris copy uses short headings and direct project language. It does not
  narrate the page's own structure or use prose to restate evidence mechanics.
- The POC evaluation includes an owner cold-open walkthrough that tests whether
  the reader can explain Butlers as a whole.

This is an additive behavioral change. It does not edit or weaken
POC-REQ-030…032: the existing narrative, provenance and Unknown obligations
continue to apply to the larger model.

## Capabilities

### New Capabilities

- `polaris-project-wide-butlers-model`: project-wide Butlers shape coverage,
  concise Polaris presentation, capability drill-down and cold-open evaluation.

### Modified Capabilities

None.

## Impact

- `packages/three-surface-poc-core`: the model gains project-shape source,
  coverage and catalog facts derived from the configured Butlers revision.
- `apps/three-surface-poc`: Polaris becomes the project-level entry and retains
  the existing capability material as drill-down.
- `GET /api/poc`: the same project-wide facts and coverage denominator become
  machine-readable; human/machine parity remains mandatory.
- Tests gain exhaustive source, coverage, parity, plain-copy and cold-open
  evaluation oracles.

## Scope

In scope is the single configured Butlers repository. “All of Butlers” means
all project shape declared by its authoritative project artifacts: purpose and
boundaries, architecture, V1 scope and success criteria, and the declared
staffer, domain-butler, module, connector and major-interface catalogs.

Out of scope: reading arbitrary implementation-file contents; claiming that
every source file or active proposal is a project capability; inferring missing
capabilities; modifying Butlers; supporting another project; production
release; autonomous behavior; multi-user support; or weakening visible Unknown,
provenance, parity, authentication or one-repository POC boundaries.

## Authority and sign-off

This is a candidate change. It binds nothing and authorizes no implementation
until the owner signs it off. The six signed
`three-surface-poc-experience` artifacts remain unchanged at their recorded
digests.

## Authoring evidence

- `CAPABILITY-COVERAGE.md` accounts for all 12 declared capability obligations.
- `CONTRACT-COVERAGE.md` partitions all 324 accepted RFC 0001–0009 clauses.
- `GOVERNING-DEPENDENCIES.md` is generated from the 11 requirement warrant
  blocks.
- `docs/reviews/R-POC-OWNER-WALKTHROUGH-POLARIS.md` records the product finding
  that triggered this change.
