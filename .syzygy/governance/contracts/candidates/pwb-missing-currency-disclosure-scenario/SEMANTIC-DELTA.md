# Semantic delta — missing effective currency bound outside freshness

> **Candidate — binds nothing.** These bytes were drafted under the owner's
> 2026-09-21 direction in
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
> row P-69, arm B, question 7a. That direction is not a specification
> amendment act. Only a dedicated owner act naming this package's exact
> manifest digest may amend the signed PWB behavioral package. This candidate
> performs no act, authorizes no implementation and edits no signed byte.

**Artifact(s):** the eleven-artifact signed
`openspec/changes/polaris-project-wide-butlers-model/` behavior subject.
Proposed bytes exist only as six unified diffs under `proposed/`; five subject
rows remain byte-identical.

**Stable IDs affected:** `PWB-REQ-007`. No requirement, contract clause,
reason, tier, freshness value or identity is minted, retired or renumbered.

**Change class:** **Normative**, not Clarifying. The owner named the instrument
a clarification scenario; the classification follows the changed obligation,
not that label. A renderer that previously satisfied PWB-REQ-007 only by
force-fitting one of four freshness values onto an unbounded claim would no
longer comply, while a renderer omitting freshness for that condition would
be newly admitted. Someone who complied before may not comply after, so the
template's Normative definition applies. [Observed: proposed scenario and the
template's class table; Inferred: compliance consequence.]

**Author:** Codex drafting worker for `syzygy-dov.20`.

**Date:** 2026-09-22

## Current meaning

[Observed] PWB-REQ-007 currently requires, without an exception:

> Every project entity and project-fact claim SHALL have a stable semantic Claim
> identity plus an evaluation instance, be challengeable with resolvable support, and carry the
> closed label, tier, exactly one primary reason, zero or more closed secondary
> reasons, freshness, challenge state and evaluation identity that govern it.

Its falsifier includes:

> a tuple field is absent/out of vocabulary

Its existing missing-evidence scenario concludes:

> - **AND** its tier, freshness and evaluation identity remain visible

[Observed] RFC2-9 supplies the fail-closed result and owner-act predicate:

> an undeclared bound renders the class's claims Unknown
> (`no-currency-bound-declared`)

and:

> A currency bound present in the tree without an effective owner act does not
> unblock its class: the claims continue to render Unknown

[Observed] RFC2-10 closes the freshness vocabulary and supplies the route the
owner selected:

> **Four values, closed.** The list changes only by amendment to this RFC; no
> implementation may mint, spell, or force-fit a freshness value it does not carry.

and:

> A condition genuinely outside the four is disclosed as a fact of the render,
> never dressed as a freshness state.

[Observed] CAP1-REQ-062 requires the Unknown result and exact reason but assigns
no freshness value to the missing-bound arm:

> a claim class with no declared currency bound renders `Unknown` with
> reason `no-currency-bound-declared`.

[Observed] RFC2-24's reason row gives the exact resolution route: `Declare the
bound in quality policy`.

## The tension being resolved

[Observed] PWB-REQ-007 demands a freshness slot on every project claim while
RFC2-10 forbids dressing a condition outside its four values as freshness.
The Capability 1 judge reflects the latter boundary: its
`no-bound-declared` result carries label and reason but no `freshness` field.
The M2 funnel recorded this as Q7 rather than selecting a value in
implementation.

[Observed] The owner chose arm B: disclose the missing RFC2-9 bound outside the
freshness slot, keep the claim Unknown, and use a CC-REV-2 scenario to
PWB-REQ-007. This delta does not call that direction an amendment act; it turns
the direction into a reviewable candidate whose exact bytes still need a
separate owner act.

## Proposed meaning

The following scenario is inserted under PWB-REQ-007 immediately before its
existing missing-current-evidence scenario:

> #### Scenario: No effective currency bound is disclosed outside freshness
>
> - **WHEN** a project claim's class has no currency-bound declaration with
>   effective owner-act provenance at the evaluation's as-of instant
> - **THEN** the claim renders `Unknown` with primary reason
>   `no-currency-bound-declared`, exposes the exact resolution route `Declare
>   the bound in quality policy`, and retains its tier, challenge state,
>   semantic claim identity and evaluation identity
> - **AND** the missing effective bound is disclosed as a named, expandable fact
>   of the render outside the claim's freshness slot; no `fresh`, `stale`,
>   `broken`, `superseded` or fifth value is minted, inferred or force-fit for
>   that condition
> - **AND** for this condition only, that outside-slot disclosure is the complete
>   presentation where this requirement otherwise names freshness; every other
>   tuple obligation remains, and no aggregate absorbs the claim into a current
>   or favourable value, omits its primary reason count or hides its route

[Observed] The proposal and capability-coverage row receive the same narrow
exception. The scenario adds no `warrants` block, so the dependency authority
union remains 17 requirements and 96 distinct authorities; only its source
digest changes.

[Observed] Five existing contract-coverage judgments are no longer honestly
`covered:PWB-REQ-007`: RFC6-14.r1, RFC6-14.r3, RFC6-17.r1, RFC7-16.r1 and
RFC7-33.r1. The proposed repair delta marks each `unknown-uncovered`, and the
generated contract coverage changes from 137 covered / 237 Unknown uncovered
to 132 / 242. This does not amend any RFC. It makes the gap visible.

## What explicitly does NOT change

1. [Observed] RFC2-9, RFC2-10, RFC2-24, RFC6-14, RFC6-17, RFC7-16 and
   RFC7-33 remain byte-identical. The PWB spec does not override a contract;
   the five newly visible coverage gaps remain contract obligations for any
   later implementation authorization to resolve or expressly route.
2. [Observed] CAP1-REQ-062 and the Capability 1 currency judge remain
   byte-identical. No freshness is added to the no-bound result.
3. [Observed] The four-value freshness vocabulary and twelve-value Unknown
   reason vocabulary remain closed. No fifth value or thirteenth reason is
   proposed.
4. [Observed] No implementation, test, registry, policy, consent, topology,
   doctrine, act record or recorder is changed by the proposed subject.
5. [Observed] The proposal's other obligations, all other PWB requirements,
   and the other ten rows of the eleven-artifact subject retain their stable
   identities. Six rows change bytes; five do not.
6. [Observed] The scenario applies when a bound is absent **or present without
   effective owner-act provenance**. A valid effective bound proceeds through
   RFC2-9's ordinary currency assessment and is outside this scenario.
7. [Observed] Aggregates retain no headline status and still disclose separate
   primary and secondary reason counts. This scenario forbids favorable
   absorption; it does not make an aggregate a claim.
8. [Observed] No timer, background poller or ambient-clock transition is
   introduced. Currency is judged at the evaluation's identified as-of
   instant.

## Warrant

[Observed] The owner ruling says:

> **B** — Q7 discloses the missing RFC2-9 bound outside the freshness slot, the
> claim stays Unknown; Q7a = instrument (i), a CC-REV-2 clarification scenario
> to PWB-REQ-007, gated behind its own sign-off and act before slice 5

The same row says that until the gates are performed, "no claim renders the
disclosure route." Drafting is therefore warranted; adoption and
implementation are not.

## Evidence or decision basis

All were read at source in this drafting session:

- the P-69 owner ruling and cross-cutting gate reading;
- PWB-REQ-007 in the signed PWB specification;
- RFC2-9 and RFC2-10 in `RFC-0002/snapshot-and-evaluation-core.md`;
- RFC2-24 in `RFC-0002/rendering-vocabularies.md`;
- CAP1-REQ-062 and its conformance-tested currency judge;
- CC-REV-2 and the candidate normative-change workflow/template;
- the M2 funnel's Q7 analysis and slices S7/S8;
- every PWB sibling candidate patch currently present on `origin/main`;
- `origin/agent/syzygy-dov.18` at `4d78776`, inspected as an inert,
  unperformed checkpoint only.

## Terms introduced / retired

None. "Missing effective currency bound" is descriptive composition of
RFC2-9's existing provenance predicate and reason, not a new closed value.

## Downstream impact

`IMPACT-LEDGER.md` records the complete methods, counts and dispositions.
In summary:

- six of the eleven bound PWB subjects receive proposed patches;
- two behavior-contract digest pins become stale on any adopted PWB successor;
- the four sibling PWB spec patches are order-tested, including gate
  `syzygy-dov.21`; later generated dependencies are always regenerated;
- lane B may precede this patch directly, while lane B would need regeneration
  if the owner chose the reverse order;
- the parked `.18` registry checkpoint is neither merged nor treated as
  authority; if later performed, this scenario remains relevant to an absent
  class row or an invalid/unperformed declaration;
- current implementation consumers do not change on this candidate branch and
  therefore render no new route.

## Migration / supersession plan

1. Freeze this candidate's exact bytes and run independent classification,
   fidelity, impact and builder review using `REVIEW-BRIEF.md`.
2. Retain raw output verbatim and disposition every finding. Any semantic
   repair retires the reviewed head and requires exact-byte reconfirmation.
3. The owner alone may perform
   `SIGN OFF PWB MISSING-CURRENCY DISCLOSURE SCENARIO: <manifest sha256>`.
   The recorder and aggregate record are adoption-time artifacts, not drafted
   here.
4. In the same adoption change, apply the six patches, regenerate the package
   against the actual predecessor, regenerate both generated files, record the
   act, add the chosen successor-chain link, and prove all eleven rows against
   the post-apply tree.
5. A separate implementation continuation is still required. The P-69 M2
   slice also waits for the registry act at `.18`, continuation at `.19`, and
   lane-B disposition at `.17`. This spec act grants none of those.
6. Rollback is a reviewed, signed successor. Performed records and prior
   manifests remain immutable history.

## Composition

[Observed] The builder applies this spec patch with the exact-source,
machine-view and `.21` opening-band patches in both orders and requires
byte-identical final spec bytes. Lane B first then this package applies. The
reverse raw order deliberately fails because lane B's wide hunk spans the
same PWB-REQ-007 region; if this package were performed first, lane B is the
later package and must regenerate against actual predecessor bytes.

[Observed] The exact-source capability-coverage patch composes with this
package in both orders. Every sibling `GOVERNING-DEPENDENCIES.md` patch
collides because each replaces one generated source-digest line; that is a
regeneration obligation, not a conflict resolved by choosing a stale patch.

## Review

**Required class:** CC-REV-1 deterministic observation/public interface,
CC-REV-4 material normative amendment, CC-REV-6 retained findings, plus an
independent classification decision.

**Reviewer:** pending fresh-context review commissioned by `REVIEW-BRIEF.md`.

**Verdict:** pending. No verdict is inferred from passing scripts.
