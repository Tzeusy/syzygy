> **Candidate — binds nothing.** A form, offered alongside the candidate
> knowledge-hygiene policy. The obligation to *use* it is that policy's
> CC-KNOW-7, which binds only through its own owner craft-amendment act. Using
> the form before then is good practice, not compliance.

# Semantic-delta template

**Companion:** [`NORMATIVE-CHANGE-WORKFLOW.md`](NORMATIVE-CHANGE-WORKFLOW.md)
— the workflow this form sits inside, the change classes, and a worked
example.

## When a delta is required

Any change to text in the **active-authority lane**: doctrine, contract
clauses in force, current policy, topology once an act accepts it, owner
decisions. Not required for
governed presentation, historical, evidence or derived artifacts — though the
change-class discipline is useful there too, and a derived artifact that
turns out to carry an obligation was never derived.

**An agent may draft a delta; adoption belongs to the owning authority.** The
delta is the proposal, never the act.

## Scope and non-scope of this file

**Scope:** the fields one proposal records, and what each field is for.
**Non-scope:** the process around the form (the workflow file owns it); the
owner acceptance ceremony for gate-bound artifacts (the active acceptance
record owns it); where deltas are stored — deliberately unspecified, a
round's delta register and a per-change file are both fine.

---

## The form

Copy the block below. **Every field is required.** `n/a` with a reason is an
acceptable value; an empty field is not.

```markdown
# Semantic delta <ID> — <short title>

**Artifact(s):**         <path(s)>
**Stable IDs affected:**  <clause / rule / decision IDs, or "none — new material">
**Change class:**         Editorial | Clarifying | Normative | Structural
**Author:**               <who drafted this>
**Date:**                 <YYYY-MM-DD>

## Current meaning
<What the text means today. Quote the exact current text for each ID.
Quote it — do not summarize it. A summary here is the first place a
semantic change can hide.>

## Proposed meaning
<What it will mean. Quote the exact proposed text.>

## What explicitly does NOT change
<Enumerate. This field exists because "I only touched X" is the most common
false claim in normative editing. Name the neighbouring obligations a reader
might reasonably assume moved, and state that they did not.>

## Warrant
<Why this change is authorized: an owner ruling, a decision, a review
finding, a contradiction that must be resolved. "It reads better" is a
warrant only for an Editorial delta.>

## Evidence or decision basis
<The artifact this rests on, with a resolvable reference. If the basis is not
reachable by everyone who can reach the artifact, say so — that is itself a
finding (CC-KNOW-4).>

## Terms introduced / retired
<Any vocabulary movement, or "none". New durable terms pass the admission
test and enter the term registry (CC-KNOW-5, CC-KNOW-6); retiring or renaming
a term across artifacts needs a reviewed migration report first.>

## Downstream impact
<Every artifact that cites, derives from, or depends on the affected IDs —
including derived views, manifests and digests. State the method used to find
them (pattern sweep, dependency index, reading). "None" requires the sweep
that establishes it, run in this session (CC-KNOW-16).>

## Migration / supersession plan
<How every invalidated artifact is updated in the same logical change
(CC-REV-2). What supersedes what, when, and on whose authority. If a
digest-bound artifact is touched, name the regeneration and re-review cycle.
If material becomes superseded, name where it goes and which reading paths
drop it (CC-KNOW-14).>

## Review
**Required class:**  <per CC-REV-1 / CC-REV-4>
**Reviewer:**        <must not have authored the change or shared its session>
**Verdict:**         <recorded verbatim — never re-labelled>
```

---

## Change classes

| Class | Means | Review floor |
|---|---|---|
| **Editorial** | Typography, formatting, link repair, whitespace. **No meaning changes.** | The class claim is itself reviewed |
| **Clarifying** | The obligation is unchanged; its statement is made harder to misread. Someone who complied before still complies. | Reviewed; the delta records why the old text was misreadable |
| **Normative** | An obligation is added, removed, narrowed, or widened. Someone who complied before may not comply now, or the reverse. | Full review per CC-REV-1; owner act if the artifact is gate-bound |
| **Structural** | Material moves between artifacts, or an artifact is split or merged. **Meanings preserved, locations changed.** | Reviewed; stable identifiers preserved and mapped |

### Rules on the classes

1. **"Editorial" and "no semantic change" are reviewable claims, not
   exemptions** (CC-KNOW-8). The reviewer's job is to test the claim. Stating
   the class up front is what makes it contradictable.
2. **Class is determined by what changes in the obligation, never by diff
   size.** A one-line edit can be Normative.
3. **Structural moves preserve stable identifiers.** A clause that moves
   keeps its ID; renumbering during a move converts a Structural change into
   an untracked Normative one, because every existing citation silently
   re-points or dangles (CC-REV-7).
4. **Whole-file rewrites are exceptional** and carry a justification plus an
   old→new mapping covering every identifier (CC-KNOW-10). "Unavoidable" is
   itself a reviewable claim.
5. **Derived artifacts regenerate after source adoption, never before**
   (CC-KNOW-11). A delta does not update indexes in anticipation of its own
   approval.
6. **Contradictions are surfaced, never silently reconciled inside a delta.**
   A contradiction found while drafting is routed as a contradiction
   (CC-REV-2's doctrine carve-out; CC-REV-3).
7. **A delta touching a digest-bound artifact names its regeneration cycle** —
   manifest regeneration, record update, fresh digest-binding review — before
   it is proposed, not after it lands.

---

## Standing rule — quoting a defect must not reproduce it

Any artifact documenting a defect will quote the defect: a delta quotes the
wrong sentence, a check register quotes the malformed citation, a migration
report quotes the broken path. If the quoted text is live syntax, the
documenting artifact **becomes an instance of what it documents** and trips
whatever validates that class.

**Rule:** a quoted defect is either fenced in a code block or marked with an
explicit, disclosed exclusion — never left as bare live syntax. Exclusions
are counted and reported, so an opt-out cannot sit silently. [Observed —
three artifacts in this pass tripped their own checks this way.]

The syntactic case is the easy one. The harder case is a quoted **claim**: an
unverified assertion copied from one artifact into another propagates by
citation and cannot be fixed by fencing. Verify before quoting, whatever the
syntax (CC-KNOW-18).

## What this template does not do

- **It does not decide the change class for you.** Nothing here stops an
  author from writing "Editorial" on a Normative change. The protections are
  that the class is stated, that current and proposed meanings are quoted in
  full, and that someone who did not author it tests the claim.
- **It is barely exercised.** The first uses are this round's delta register;
  its fields remain lightly tested by practice, and an early use should be
  treated as a trial of the form as much as of the change.
- **It specifies no storage location and no tooling.**
