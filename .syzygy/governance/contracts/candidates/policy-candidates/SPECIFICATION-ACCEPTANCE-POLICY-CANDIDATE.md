# Specification acceptance policy

> **Authority depends on an exact-digest owner act, not this banner.** These
> bytes are a proposal while no performed owner Decision names their SHA-256.
> From an act that names that digest, the same bytes are the confirmed
> successor; no edit is needed. The governing Decision is selected by the rule
> below. Drafting, review, a commit, or a pull request changes no authority.
>
> IDs `CC-SPEC-1` through `CC-SPEC-11` stay stable. This policy and
> `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` form one model. The proposal,
> history, exact mapping, and review contract are in
> `../round-2026-08l/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-3.md`.

## Shared terms and results

An **acceptance unit** is either a complete capability (**whole-capability
acceptance**) or one coherent change to an accepted capability
(**focused-change acceptance**). **Requirement provenance** is the accepted
authority that explains why requirement text belongs; it is not permission to
start work. A **coverage population** is a source-enumerated set fixed before
classification. A **reviewed N/A** is an owner Decision that lawfully says one
contract consequence needs no behavioral requirement.

Every rule below returns **Satisfied** only when its decision can be reproduced,
**Not satisfied** when evidence proves a violation, or **Unknown** when required
evidence or a decision is missing, stale, contradictory, or unresolvable.
Unknown never counts as Satisfied and blocks acceptance. Each rule uses the same
format.

## **CC-SPEC-1 — Declare the capability and acceptance unit**

- **Purpose:** Bound one owner-readable product argument and one acceptance
  decision.
- **Inputs/population:** The proposed specification; for a focused change, the
  accepted baseline and exact baseline-to-proposal difference.
- **Decision:** Name one coherent capability, its scope and non-goals, then mark
  the unit `whole-capability` or `focused-change`. A focused change lists every
  obligation added, changed, retired, or made newly relevant and does not
  re-accept or widen the baseline. Apply CC-SPEC-2 through CC-SPEC-11 to either
  unit.
- **Possible results:** Satisfied, Not satisfied, or Unknown.
- **Missing evidence:** An unnamed baseline, unclear unit, or omitted obligation
  is Unknown; narrowing the stated population does not cure the omission.
- **Retained evidence:** Capability identity, unit, scope, non-goals, baseline
  digest when used, and proposal digest.
- **Sources:** SDR-37; CC-SPEC-11.

## **CC-SPEC-2 — Record complete requirement provenance**

- **Purpose:** Make every material governing authority visible without confusing
  provenance with work permission.
- **Inputs/population:** Every requirement and every normative statement that
  can supply or change its obligation, boundary, vocabulary, oracle, or scope.
- **Decision:** For each requirement, populate exactly these six fields with
  stable identities:

  ```text
  doctrine[]  contracts[]  policies[]  decisions[]  topology[]
  parent_requirements[]
  ```

  An authority is material if removing it removes an accepted basis or changes
  what the requirement may require, permit, or prohibit. Record all material
  adopted, accepted, approved, or recorded authorities; one may be primary for
  navigation. Exclude candidates and pending decisions. Generate the
  specification declaration from these fields under CC-IMPACT-1; never maintain
  a second list.
- **Possible results:** Satisfied when all and only eligible material authority
  is recorded; Not satisfied for a proved omission, ineligible entry, empty
  basis, or duplicate home; Unknown when materiality cannot be settled.
- **Missing evidence:** Record Unknown beside the requirement, name the disputed
  authority and settling evidence, and block acceptance.
- **Retained evidence:** Six-field declaration, materiality checks, primary
  marker if any, and Unknown records.
- **Sources:** VIS-2; RFC1-25; CC-REV-3. RFC1-25's `motivates` relation separately
  carries work warrants; a finding warrants work only after recorded
  confirmation and never becomes a seventh provenance field. `Lawfully admitted
  user need` remains excluded because no accepted authority defines its
  admission.

## **CC-SPEC-3 — Preserve requirement identity**

- **Purpose:** Keep citations stable through change and retirement.
- **Inputs/population:** Every requirement entry in baseline and proposal.
- **Decision:** Mint an ID once; amend in place; never renumber, reuse, or delete
  it. Mark a withdrawn requirement retired in its retained entry.
- **Possible results:** Satisfied, Not satisfied, or Unknown.
- **Missing evidence:** Untraceable continuity or a missing retired entry is
  Unknown and blocks acceptance.
- **Retained evidence:** ID inventory, baseline/proposal mapping, and retired
  entries.
- **Sources:** CC-REV-7.

## **CC-SPEC-4 — Make every requirement falsifiable**

- **Purpose:** Ensure evidence could disprove every requirement.
- **Inputs/population:** Every active requirement.
- **Decision:** Name one form—event-response, state projection/query, invariant,
  prohibition, or lifecycle transition—and state a reproducible case, observable
  consequence or violation, bounded success/failure oracle, oracle independent
  of the implementation, and concrete falsifier. For invariants and
  prohibitions, the case is the quantified population, counterexample schema,
  sweep method, and denominator. Reject tautologies, unbounded semantic
  equivalence, unreachable cases, and implementation-defined oracles.
- **Possible results:** Satisfied, Not satisfied, or Unknown.
- **Missing evidence:** An absent form, element, bound, denominator, or
  independence basis is Unknown.
- **Retained evidence:** Form, five elements, oracle procedure, population, and
  falsifier.
- **Sources:** VIS-2.

## **CC-SPEC-5 — Expose non-goals and Unknowns**

- **Purpose:** Prevent uncertainty or exclusions from disappearing.
- **Inputs/population:** Non-goals and every Unknown produced by this policy.
- **Decision:** Record each Unknown at its owning requirement, CC-SPEC-8 row or
  population section, CC-SPEC-11 `adoption-record selection` section, or
  CC-SPEC-11 row. Name the reason and settling condition. The primary human and
  machine views render the same result and link to that home.
- **Possible results:** Satisfied when every item has one durable home and parity;
  Not satisfied for a proved omission or mismatch; otherwise Unknown.
- **Missing evidence:** Missing ownership, link, or projection parity is Unknown
  and blocks acceptance.
- **Retained evidence:** Non-goals, owning records, links, and both projections.
- **Sources:** VIS-2; CC-REV-5.

## **CC-SPEC-6 — Do not decide an open shape question implicitly**

- **Purpose:** Keep specification authorship inside existing authority.
- **Inputs/population:** Every requirement and every open owner question at the
  named revision.
- **Decision:** Test whether the requirement would select an answer. The author
  records the questions believed untouched; a reviewer or owner, not the author
  alone, may settle or reclassify the test.
- **Possible results:** Satisfied when no question is selected; Not satisfied
  when one is selected without its owner Decision; otherwise Unknown.
- **Missing evidence:** An unsettled classification is Unknown and blocks the
  requirement.
- **Retained evidence:** Revision, question inventory, classifications, reviewer,
  and any governing Decision.
- **Sources:** VIS-4.

## **CC-SPEC-7 — Keep implementation detail out unless behavior requires it**

- **Purpose:** Specify observable behavior rather than an accidental solution.
- **Inputs/population:** Every stack, schema, or mechanism named by a requirement.
- **Decision:** Retain it only when changing it would change required behavior;
  otherwise remove it from the specification.
- **Possible results:** Satisfied, Not satisfied, or Unknown.
- **Missing evidence:** Unsettled behavioral necessity is Unknown.
- **Retained evidence:** Named detail and the behavior that requires it, or its
  removal disposition.
- **Sources:** `architecture.md`, Typed authority.

## **CC-SPEC-8 — Cover every applicable accepted-contract consequence**

- **Purpose:** Prevent contract prose from becoming unspecifiable behavior or
  disappearing behind a clause-level summary.
- **Inputs/population:** At one revision, read the candidate upper-bound manifest
  at `.syzygy/governance/contracts/candidates/ACTIVE-CONTRACT-MANIFEST.txt`.
  Select performed contract-acceptance Decisions by CC-SPEC-10. Match each act's
  argument digest to exactly one file under
  `.syzygy/governance/contracts/candidates/wave-manifests/`, then union those
  manifest rows. A row is accepted only when the identical `sha256  rfcs/...`
  row exists in the upper bound and the installed path made by prefixing that
  `rfcs/...` path with `.syzygy/governance/contracts/` hashes to it.
- **Decision:** Before applicability, enumerate the clause IDs declared by each
  accepted module and locate each ID's definition marker in its installed bytes;
  zero or multiple definition markers are Unknown. Tokenize from each marker to
  the next marker or file end into non-overlapping byte spans covering the whole
  range: headings, paragraphs, list items with continuations, table rows,
  blockquotes, fenced blocks, separators, and an `other syntax` fallback.
  Classify every span
  consequence-bearing, non-normative with reason, or Unknown. Split only
  separately falsifiable outcomes and assign `(clause, span ordinal, outcome
  ordinal)`. A consequence is applicable when the capability uses the entity,
  behavior, boundary, vocabulary, or interface it governs. Map each applicable
  row to requirements or to a reviewed N/A.
- **Possible results:** Satisfied when every applicable row is mapped or has a
  lawful N/A; Not satisfied for a proved omission or invalid N/A; Unknown for
  selection, path, digest, tokenization, segmentation, applicability, or mapping
  uncertainty.
- **Missing evidence:** Record Unknown in `population-construction` before rows
  exist, or in the affected row later, name what settles it, and defer
  acceptance. Select a reviewed-N/A owner Decision by CC-SPEC-10. Honor it only
  when it names the exact consequence and scope and independently kept evidence
  matches project, decision identity/digest, act type, owner, instant, scope,
  supersession, and audit-record identity; any missing or mismatched binding
  means Unknown and unmapped.
- **Retained evidence:** Revision; selected Decisions/manifests; candidate,
  accepted, and excluded counts; every path/digest comparison; clause/span/
  consequence counts; extraction method; rows, mappings, N/A Decisions, and
  Unknowns.
- **Sources:** RFC1-33, RFC3-15, RFC3-16, RFC6-28, RFC7-38, RFC8-32, RFC9-52.

## **CC-SPEC-9 — Pass fresh-reader review**

- **Purpose:** Keep the specification usable without authoring history.
- **Inputs/population:** Exact proposed bytes and their stated constraints.
- **Decision:** A reader with no authoring context accurately restates intent,
  constraints, failure paths, and exclusions.
- **Possible results:** Satisfied only by a passing independent review; Not
  satisfied by a failing review; Unknown when no valid review exists.
- **Missing evidence:** Unknown blocks adoption; record failure on the
  specification surface.
- **Retained evidence:** Exact digest, reviewer independence, raw report, verbatim
  verdict, and dispositions.
- **Sources:** VIS-3; CC-REV-4; CC-REV-6.

## **CC-SPEC-10 — Select authority and adopt only exact bytes**

- **Purpose:** Make lifecycle force reproducible without editing acted-on bytes.
- **Inputs/population:** At a named revision, every performed tracked owner
  Decision. Eligibility is purpose-specific: an adoption act names the
  specification identity and digest; a policy-confirmation act names the policy
  identity and digest; a contract-acceptance act names contract or wave
  identities and its exact manifest argument; a reviewed-N/A act names the exact
  consequence and scope; an adjudication act names the contradiction identity
  and conflicting claims. Every candidate also supplies its own Decision
  digest, act type, owner, instant, scope, and explicit supersession/revocation
  link.
- **Decision:** Select only candidates whose act type and subject fields match
  the stated purpose. Follow only explicit supersession or revocation links;
  choose the eligible Decision no other eligible Decision supersedes or revokes.
  Never use file order, commit order, or timestamp as precedence. No candidate
  means proposal or unresolved contradiction, as the purpose requires. Multiple
  incompatible unsuperseded candidates mean contradiction. Specification
  adoption records the exact specification digest and quoted content. For a
  focused change, select the proposed change separately; no proposal act changes
  the selected state of its accepted baseline. Apply VIS-4 at the adoption act:
  delegation requires both its accepted adjudication RFC and explicit doctrine
  gate-opening amendment; security, privacy/retention, and normative-data changes
  always require the owner.
- **Possible results:** Satisfied when the purpose-specific state—candidate,
  adopted specification, confirmed policy, resolved contradiction, or Unknown—
  is faithfully reported; Not satisfied for a false state claim; Unknown when
  selection cannot resolve.
- **Missing evidence:** Record contradiction in the CC-SPEC-11 table's
  `adoption-record selection` section with revision, records/digests, missing
  relationship, and settling owner Decision. Render and link the same Unknown;
  do not adopt or enumerate it as accepted.
- **Retained evidence:** Candidate set, selection trace, exact digest and quote,
  act authority, supersession links, and Unknown section.
- **Sources:** VIS-4; RFC3-15; RFC3-16.

## **CC-SPEC-11 — Demonstrate coverage of the acceptance unit**

- **Purpose:** Prove that the specification covers its own declared obligations;
  CC-SPEC-8 separately covers contract consequences.
- **Inputs/population:** Tokenize scope, change scope, and non-goals into numbered
  items, bullets, table rows, or normative prose sentences; split only separately
  falsifiable outcomes. Include every stable requirement entry, including
  retired entries. Whole-capability input is all scope items, requirements, and
  non-goals. Focused-change input is every added/changed/retired requirement,
  every change-scope item and non-goal, plus every unchanged baseline requirement
  classified by a recorded sweep as affected, unaffected with reason, or
  undecidable after testing references, provenance, mappings, and defined
  vocabulary.
- **Decision:** Preserve every extracted occurrence with revision, exact locator,
  span, and discovery method. Group only identical `(revision, locator, span,
  outcome)` occurrences; stable IDs link evidence but do not erase distinct
  occurrences, and semantic similarity never deduplicates. Give other items
  `(section, unit ordinal, outcome ordinal)` IDs. Place each row exactly once in
  `covered`, `lawfully out of scope / retired`, or `Unknown / unresolved`.
  Scope rows name satisfying requirement IDs; active requirement rows link to an
  independently extracted scope/change row and never cover themselves; non-goals
  conflict with no active requirement; retired rows retain their ID and entry;
  affected-baseline rows link to the change. Missing, circular, or contradictory
  relationships are Unknown. A party other than the author reproduces and
  confirms the population and partition.
- **Possible results:** Satisfied only when every row is covered or lawfully out
  of scope/retired, every applicable CC-SPEC-8 row is mapped or lawful N/A, and
  no provenance Unknown remains; Not satisfied for a proved violation; otherwise
  Unknown.
- **Missing evidence:** Record every blocking row and settling condition, defer
  acceptance, and leave the proposed unit a candidate. No exception converts
  Unknown to acceptance.
- **Retained evidence:** Baseline/proposal digests, extraction and affected-
  baseline methods, all occurrences and rows, mappings, three-set totals,
  reviewer, result, and adoption-selection section.
- **Sources:** VIS-2; CC-SPEC-1; CC-SPEC-3; CC-SPEC-8.
