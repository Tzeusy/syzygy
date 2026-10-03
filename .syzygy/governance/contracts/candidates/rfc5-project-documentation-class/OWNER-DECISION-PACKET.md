> **Candidate — binds nothing.** This packet offers a contract amendment for
> the owner's decision. It performs no act, adopts nothing and authorizes no
> implementation. It carries no digest by design: the argument of an act is
> derived from the manifest by script, never transcribed.

# Owner decision packet — RFC-0005 `project-documentation` content class

Status: candidate, **not yet offered**. No fresh-context review has confirmed
these bytes (`REVIEW-BRIEF.md`). Nothing below is performed by replying, by a
commit or by a merge.

## What this decides

Whether RFC5-14's closed content-class vocabulary gains a seventh class,
`project-documentation`: a project's own reader-facing prose (README, guides,
tutorials, overview documents, changelogs, contribution guides, licence and
notice files) that does not govern the project's development. You chose this
on 2026-10-03 as Q7 option (a) of the public-repository admission packet.

## What it changes

One accepted module, `rfcs/RFC-0005/consent-egress-secrets.md`, gains a table
row and one bullet in RFC5-14. The bullet says the declared classification
policy decides membership per file, a file it cannot place fails closed, a
consent that does not list the class does not permit it, and the amendment adds
no class ordering and leaves secret screening untouched.

## What it does not change

- The six existing classes, the composite rule, RFC5-15's check, RFC5-16
  screening, or the rule that the classification policy binds only under
  RFC3-16(a).
- Any consent. No record gains the class; the admission egress record lists
  five classes and would need a further version naming this one.
- Nothing is read, sent or implemented. Without this class the Redis
  licence-history proof (which needs LICENSE) and README-driven pages cannot
  run; code-only pages can.

## The decision

**(a) Yes — as drafted.** A fresh-context review runs; findings are repaired;
the act is offered once a round confirms the exact bytes.
**(b) Yes, with named changes.** Say which sentence differs; the package is
redrafted and reviewed again.
**(c) No.** RFC5-14 stands; documentation stays unsendable, and public-target
pages run on code and specifications only.

## Which act form (a question for the sitting, not a recommendation to skip)

Which digest an act binds depends on the form, and for this one-row manifest
the two digests differ: the manifest file's digest (what the manifest header
and a typed phrase name) and the manifest row's digest (the proposed-bytes
digest, what the 2026-10-02 re-pin form names). Option 1 binds the row,
option 2 the file, option 3 neither (a version tag). Three forms are
available:

1. **Option selection naming the record at its manifest row**, the form you
   gave for the admission records and the 2026-10-02 policy re-pin. No phrase
   or digest to read; a recorder binds the act to the row. *Recommended for
   this sitting* because you are already giving acts in that form. [Inferred]
   This would be the first accepted-contract amendment given that way; the
   re-pin precedent covered a policy and a registry entry.
2. **A typed contract act phrase over the manifest digest**, as earlier
   accepted-contract amendments were given. Slower, the most precedent.
3. **The version-tagged sign-off of the 2026-10-02 Scope A direction.** [Inferred]
   Not obviously available: that direction names PWB specification deltas, the
   observer registry entry and "the contract successors queued behind them",
   and this amendment is queued behind none of those. If you read Scope A as
   reaching it, say so; that is a ruling, not something this packet assumes.

Whichever you choose, a recorder and the registration of its phrase or label in
`scripts/check_governance.py` are prepared after a confirming review, against
the confirmed commit, as for the admission package. The install step (applying
the patch to both mirrors and regenerating what CG-7h and the contract index
name) belongs in the same change as the act record.

## One consequence to know

`openspec/changes/polaris-manifesto-generation/SOURCE-POLICY.md` says in the
present tense that "The egress vocabulary remains" the six classes. It is
bound by performed acts and cannot be edited here. After adoption that
sentence is false on a default reading path, and the contract workflow
(step 6) requires such an artifact to be updated in the same change. The only
lawful update is a readability successor, which needs your sign-off. Your
choices: direct that successor with the adoption (follows step 6), or leave
the file as is, which departs from step 6; the departure is disclosed in
`SEMANTIC-DELTA.md`, and the specification clause that binds (REQ-025) cites
the vocabulary by reference. The package does not choose.
