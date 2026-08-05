> **Approved** — owner decision D2 (2026-08-01), amendment B21 applied where noted. **This directory (`.syzygy/governance/policies/craft-and-care/`) is the canonical home of these policies.** The bootstrap-phase copy is preserved separately as historical review evidence. Binding force on implementation work begins with the owner's digest-bound acceptance of the foundational design contracts (the act defined in the active acceptance record; the policies cite RFC clauses that bind nothing until then).

# Review and documentation

Baseline: the canonical bar's review discipline (cite the violated
expectation with evidence; severity follows blast radius; independent review
preserved when a reviewer authors semantic changes) and same-change
documentation bias apply by reference. Syzygy's additions concern *which*
changes must be independently reviewed, and how documentation stays a single
truthful authority.

## CC-REV-1 — Mandatory independent review classes

Changes touching any of the following classes require review by an
independent, fresh-context reviewer — one who did not author the change, does
not share the authoring session's context, and receives the artifact, its
governing doctrine/RFC references, and acceptance criteria, not the author's
reasoning or a desired verdict:

1. **authority boundaries** — write-universe, typed-authority table,
   adapter authorization (VIS-5, VIS-6);
2. **graph identity** — entity identity minting, continuity, split/merge
   (SDR-2, SDR-22 identity-based counting);
3. **deterministic observation** — snapshot composition, evaluation
   identity, the deterministic/inferred seam (VIS-7);
4. **security** — anything under SEC-1…SEC-5, auth surfaces, egress paths;
5. **data migration** — `.syzygy/**` schema migrations, any
   identity-affecting store change;
6. **public interface** — machine-queryable endpoints, adapter contracts,
   anything an external consumer can depend on;
7. **certificate logic** — when certificates exist (post-V1,
   future-tagged), any code that grants, invalidates, or renders them.

**Class membership is contested by default and is never finally determined
by the agent performing the change** (mirroring VIS-4's classification
rule): the change record states which classes the change touches, or
"none," so a misclassification is a findable violation after the fact, and
a reviewer or the owner may reclassify at any time. Self-declared
complexity never exempts these classes (CC-BAR-6). The implementing agent
never reviews its own change here, and per the canonical bar, if the
reviewer authors semantic fixes, the exact resulting head gets fresh
independent review. To keep steering out of the channel context isolation
cannot close, review prompts for these mandatory classes are **standing
artifacts** (maintained like the bootstrap's `review-prompts/`), not
per-review authored text — the author's side may select the artifact
cluster, never compose the reviewer's instructions.

*Violation:* an agent modifies snapshot hashing "as a refactor," self-reviews
because the diff is small, and merges — a class-3 change with no independent
eyes.

## CC-REV-2 — The same-logical-change rule

A change that invalidates any authoritative artifact updates **every**
invalidated authoritative artifact in the same logical change: behavioral
specs (`openspec/`), declared topology, accepted contracts, and the policies
in this cluster. "We'll sync the spec later" is a violation, not a plan
(canonical bias 7, strengthened to *all* typed authorities). [Observed —
FD-020 E1-b (done includes same-change spec update, topology when structure
moved) and E10 (same-change-mandatory sync).] The rule is a **merge
invariant, not a property of how work is packaged**: no merge may leave
mainline with an invalidated authoritative artifact still asserting the old
truth. Splitting one logical change across sequenced merges that pass
through such a state *is* the violation — an open follow-up PR is "syncing
later" by another name.

The one structural carve-out: **doctrine** is amended only through the owner
gate (VIS-4). When a change would invalidate doctrine text, the change stops
and routes to the owner as a contradiction — it does not edit doctrine
in-change, and it does not merge while the contradiction is open.

*Violation:* moving a responsibility between two surfaces, updating code and
specs, and leaving declared topology asserting the old placement — creating
exactly the intent-vs-observed drift Syzygy exists to expose.

## CC-REV-3 — No hidden duplicate authority

Every fact has exactly one authoritative home per the typed-authority table;
everything else is a labeled, rebuildable projection or an explicit citation
(VIS-6; FD-020 E4-d rejects second sources of truth). In practice:

- documentation **cites** authoritative artifacts, it does not restate them
  normatively — a restated rule drifts and becomes a shadow authority;
- no cache, index, view, or surface-local store may be the only holder of a
  truth-bearing fact; surfaces are never independently authoritative
  (architecture.md, one kernel);
- discovering the same question answered in two homes is a contradiction to
  surface, never a precedence call to make silently.

*Violation:* a surface keeps its own "effective capability list" that is
edited directly when the declared artifacts lag — a second authority hidden
inside a projection.

## CC-REV-4 — Fresh-reader review for normative artifacts

Every normative artifact passes fresh-reader review at adoption and on
material amendment (VIS-3): a reader with no authoring context restates
intent and constraints correctly, and failures are recorded on the
artifact's surface. Scope per SDR-14: material changes and release
milestones, not every prose correction. Two failed review rounds signal
upstream ambiguity — return to the source decision, don't polish prose.

*Violation:* a contract amended in five successive LLM sessions, each edit
locally reasonable, none fresh-reader-reviewed, until only its authors can
parse it.

## CC-REV-5 — Epistemic labels in documentation

Substantive claims in engineering documentation carry [Observed] (with a
resolvable source), [Inferred], or [Unknown]; the labels are exclusive, and
missing evidence renders Unknown, never Inferred
[Observed — trust-and-evidence.md]. Narrative may blend, but provenance must
be recoverable at the point of consumption, and generated prose is a
non-citable editorial draft until a human adopts it (SDR-15).

*Violation:* a design doc stating "the adapter layer handles reconnection
transparently" about behavior nobody has observed — an [Unknown] wearing
declarative prose.

## CC-REV-6 — Review findings are dispositioned, never dropped

Raw reviewer output is stored unchanged before synthesis. Every
revise-severity finding is either fixed or explicitly overruled with recorded
rationale by the accountable authority (the owner, for owner-gated
artifacts). A useful review names concrete risks even when accepting;
rubber-stamp reviews are themselves findings.

*Violation:* a synthesis that quietly omits the one reviewer finding the
author disagreed with, leaving no record it was raised.

## CC-REV-7 — Identifiers are stable; retire, never renumber

Policy numbers, rule identifiers, decision numbers, and RFC numbers are
stable after adoption: amend text in place; retire rather than renumber
(mirrors doctrine's identifier rule). A retired identifier's entry remains,
marked retired, so historical citations still resolve.

*Violation:* deleting a retired `CC-DEP-2` and shifting `CC-DEP-3…7` up by
one, silently re-pointing every existing citation at the wrong rule.
