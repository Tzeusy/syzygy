# Owner direction — Three-Surface POC mode

Date: 2026-08-29

Owner: Tzeusy

Baseline: `4ee5847bd68344d671e72677b828dd5520cecb21`

The owner directly authorizes a non-release, deliberately bounded proof of
concept across Polaris, Trajectory, and Orrery, using Butlers as the initial
external proving project. For this experiment only, this direction supersedes
the Capability-1-only and no-external-project-onboarding restrictions that
preceded it. Implementation outside Capability 1 is authorized only where the
experiment requires it.

The experiment tests whether one shared project model makes one real software
capability substantially easier for an unfamiliar engineer and its owner to
understand and operate. It must demonstrate desired intent, human-triggered
work, a worker-authored real code/test change, an unverified intermediate
state, captured test evidence, verification against the named intent revision,
cross-surface navigation, visible Unknown regions, and a machine-queryable view
of the same facts.

The following invariants remain in force:

- desired, execution, and observed state remain distinct;
- no evidence means Unknown;
- activity or merge state is never intent satisfaction;
- human and machine views consume one shared fact model;
- every positive claim has resolvable provenance;
- work dispatch is human-triggered; and
- Syzygy does not write implementation code.

This direction does not authorize production release or deployment,
autonomous adoption of intent, broad remote access, multi-user support, or
changes to adopted doctrine or accepted contracts. The POC has at most eight
outcome-oriented work items, WIP one for shared-model changes, and one bounded
product-review cycle: one independent review, one consolidated repair, and one
confirmation. Non-blocking findings are deferred briefly. The experiment must
not be represented as conforming, complete, or released.

No RFC, OpenSpec change, launch packet, questionnaire, acceptance ceremony, or
review round is created for this direction.
