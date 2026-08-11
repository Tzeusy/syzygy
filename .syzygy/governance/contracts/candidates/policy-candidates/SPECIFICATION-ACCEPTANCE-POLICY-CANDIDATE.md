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

**CC-SPEC-2 — Every requirement names its lawful higher-level warrant.**
A requirement traces upward to exactly one of these, **and names which**:

```text
adopted doctrine                 by rule ID
accepted contract                by clause ID
recorded owner product decision  by decision identifier or path
accepted parent specification    by specification and requirement ID
lawfully admitted user need      by the record that admitted it
```

A requirement serving nothing on this list is a finding against the spec,
not a bonus. *(Widened 2026-08-11, owner charter §9. The clause previously
admitted only doctrine rules and contract clauses — a rule narrow enough
that a requirement implementing a **recorded owner decision** had no lawful
warrant to cite, and the first specification is full of them: P-31, P-36,
P-37, P-38 and P-40 are all owner rulings that Capability 1 must implement
and no contract clause states. Naming which kind of warrant is the part
that keeps the widening honest: five admissible sources with no obligation
to say which would be no constraint at all.)*

**CC-SPEC-3 — Every requirement has a stable identity.** Identifiers are
minted once, amended in place, never renumbered or reused — the corpus's
identifier discipline extended to specs.

**CC-SPEC-4 — Observable requirements name success *and* falsification.**
A testable observable requirement names four things:

```text
initiating condition      what happens, or is done, to trigger it
observable result         what is then visible, and where — human view,
                          machine endpoint, or both
positive success oracle   how one decides the result IS the expected one,
                          without judgment
falsifying evidence       what would show it failed or is absent
```

A requirement whose satisfaction no evidence could ever contradict is not a
requirement. *(Restated 2026-08-11, owner charter §9. The clause already
required the initiating condition, the observable outcome and the absence
evidence; the **positive success oracle** is the addition. "The outcome is
visible" is not an oracle — two reviewers can both see something and
disagree about whether it is the expected something, and a spec that leaves
that to judgment has moved the vibe check from acceptance to testing.)*

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

**CC-SPEC-10 — Lawful adoption is recorded at the exact digest.**

> Lawful adoption under VIS-4 is recorded at the exact digest. Under the
> current doctrine state, this means owner adoption.

Until that record exists the spec is a candidate like everything else, and
the record quotes what was adopted at which digest. *(Restated 2026-08-11,
owner charter §9. The clause previously hard-coded owner-only adoption
forever. VIS-4 governs delegation and may define a future gate that is not
the owner personally; a craft rule that contradicted doctrine's own
delegation clause would have to be amended the day doctrine exercised it.
The rule now defers to VIS-4 and states the current reading of it, which is
the same thing today and the right thing later.)*

## What this policy is not

Not a workflow (the th-projects feature-request workflow is referenced
process, never authority); not a format (P-39 owns the medium); not a
review procedure (CC-REV-1/2/4 own review). One fact, one home.
