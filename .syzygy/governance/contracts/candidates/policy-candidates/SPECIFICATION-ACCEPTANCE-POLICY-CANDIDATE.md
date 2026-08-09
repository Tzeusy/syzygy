# Specification acceptance policy — candidate craft rule set

> **Candidate. Binds nothing until its own `CONFIRM CRAFT AMENDMENT`
> act.** Proposed at the 2026-08-10 launch-closure pass to close
> launch-gate question E5 (no acceptance criteria existed for a
> specification itself — "spec acceptance would be a vibe check").
> Identifiers `CC-SPEC-1…10`; amended in place, never renumbered. The
> testability sub-criterion (CC-SPEC-4) is the one E5 limb that had no
> criterion even in candidate form before this file.

## The rule

**CC-SPEC-1 — Capability and scope are clear.** The specification names
one coherent capability (per the granularity rule, P-40), what is in it,
and what is out. A reader can say what the capability is in one sentence
without reading the requirements.

**CC-SPEC-2 — Governing vision and contracts are cited.** Every
requirement traces to the doctrine rule and/or accepted contract clause
it serves, by identifier. A requirement serving nothing citable is a
finding against the spec, not a bonus.

**CC-SPEC-3 — Every requirement has a stable identity.** Identifiers are
minted once, amended in place, never renumbered or reused — the corpus's
identifier discipline extended to specs.

**CC-SPEC-4 — Observable requirements have testable scenarios.** A
requirement is testable when it names: the observable surface (human
view, machine endpoint, or both), the initiating condition, the expected
observable outcome, and the evidence that would show the outcome absent.
A requirement whose satisfaction no evidence could ever contradict is not
a requirement.

**CC-SPEC-5 — Non-goals and Unknowns are explicit.** What the capability
deliberately does not do is listed; what is not yet known renders
Unknown with its reason, never silently omitted (VIS-2 applied to the
spec itself).

**CC-SPEC-6 — No unresolved shape decision is silently selected.** If a
requirement's content would settle an open owner question, the spec is
blocked on that question — authoring around it by implication is the
violation this rule exists to name.

**CC-SPEC-7 — Implementation detail appears only when it is required
behavior.** A stack, schema, or mechanism appears in a spec only if the
behavior being specified is genuinely about it; otherwise it belongs to
implementation, later.

**CC-SPEC-8 — Applicable contract clauses are covered or lawfully N/A.**
The clause-to-requirement coverage matrix (the phase-rule clauses'
obligation) is produced with the spec; every applicable clause is covered
by a requirement or carries a reviewed N/A judgment whose home and
provenance follow the corpus's reviewed-N/A rule.

**CC-SPEC-9 — A fresh technical reader can restate it.** A fresh-context
reader (CC-REV-4's standard) can restate the capability and its
acceptance conditions without authoring context; failure to restate is a
finding against the spec's comprehensibility, not the reader.

**CC-SPEC-10 — Owner adoption is recorded.** The spec binds only from a
recorded owner adoption (VIS-4); the record quotes what was adopted at
which digest. Until then it is a candidate like everything else.

## What this policy is not

Not a workflow (the th-projects feature-request workflow is referenced
process, never authority); not a format (P-39 owns the medium); not a
review procedure (CC-REV-1/2/4 own review). One fact, one home.
