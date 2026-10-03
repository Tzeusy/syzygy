# Impact ledger — public-source screening scope, version 2

> **Candidate — binds nothing.** Drafted 2026-10-04.

## What the act breaks

Same set as version 1, because both acts replace the policy digest and
version: the Butlers read gate pins the policy by digest and then version and
refuses on any byte change. The version-1 package's ledger and its simulation
script list the set; this act re-points the same files a second time. Order
with version 1 is packet Q2. [Unknown] Whether the set changed between the
version-1 ledger and the act; the installer derives it from the recorded act
at the sitting rather than from this page.

## Population this rule can reach

[Unknown] What any target repository contains; no body was read. The fixtures
in the builder are the only evidence about which paths match, and they are
about names, not content.

## What is unchanged

Secret detectors, active-content rule, access boundary, raw-body handling,
`work-history` never classified, `governance-text` and `evidence-content`
unmapped.

## Code consequence, not in this package

Implementing the rule (a consumer that reads `rules` and applies the ASCII-fold
path match) is out of scope here and goes to the implementation lane after the
act. The reference reader in the builder is the oracle that code is tested
against.
