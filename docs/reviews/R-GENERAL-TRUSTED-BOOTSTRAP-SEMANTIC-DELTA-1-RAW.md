**REVISE**

Bound to semantic-delta sha256 `0c52028dda84f3613a143bd82a36b45dbadbfdacd474f57de115707370cd3bda`, baseline `20e5b6e7c512436b67dec9eb05e0ee926096a7b5`.

Revise findings:

1. **State-(1) formation is materially ambiguous.** The proposed state-(1) replacement omits the current requirements that it preserve the exact owner phrase, exact digest, and recording commit/tag, and does not resolve whether state (1) remains limited to acts performed before A1 exists ([delta](</home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-general-trusted-bootstrap/.syzygy/governance/contracts/candidates/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-SEMANTIC-DELTA.md:121>)). Retain those positive ceremony requirements explicitly, decide the post-A1 case, and amend RFC3-16(b)'s “A verifiable owner act binds” introduction. If state (1) remains available after A1 ships, it must require an explicit owner choice—never automatic fallback from failed A1.

2. **RFC2-13 conflates owner acts with kernel facts.** The candidate says “challenge resolutions” require an effective owner act. RFC2-13 distinguishes:

   - authorization-bearing latency/resolution/sweep policies;
   - actual human resolution acts; and
   - kernel-recorded admission, rejection and deterministic sweep-resolution facts.

   The last class is `kernel-recorded`, never adopted and never an owner act. Amend only the authorization-bearing policies and resolution decisions to accept state (1); preserve kernel records as evidence/facts carrying the policy's authorization provenance.

3. **The warrant/evidence boundary is only stated in one direction.** The delta says unverifiable evidence is not converted into an owner act, but must also state the converse: an effective owner act is a warrant, never evidence that an effect succeeded, a claim is true, completion occurred, effects were applied, recovery worked, or a release gate passed. A1 correlation and RFC5-25 audit evidence establish provenance/occurrence, not substantive success.

4. **RFC9-45 cannot acquire a nonexistent deployment/recovery contract.** The delta says deployment/release “still requires” an explicit act and recovery obligations while separately acknowledging that no accepted general recovery-effect contract exists ([lines 185–193](</home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-general-trusted-bootstrap/.syzygy/governance/contracts/candidates/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-SEMANTIC-DELTA.md:185>), [245–246](</home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-general-trusted-bootstrap/.syzygy/governance/contracts/candidates/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-SEMANTIC-DELTA.md:245>)). RFC9-45 is a walkthrough/release-policy gate, not a generic deployment authorization or recovery contract. State instead that this amendment creates no deployment/recovery authority; those effects remain unavailable until separately contracted, specified and authorized.

Other conclusions:

- [Observed] The owner interpretation act lawfully satisfies candidate RFC10-24's explicit owner-ruling alternative. No doctrine amendment is additionally required for bounded missions, but RFC10 acceptance, signed OpenSpec behavior and all mission gates remain prerequisites.
- [Observed] The accepted/candidate direct-contradiction set is substantially complete.
- [Observed] The seven baseline denominators reproduce independently by both `git grep` and `rg`-equivalent archive inspection: `191/45/37/6/19/22/6`.
- [Observed] The candidate preserves two provenance states, rejects A1 downgrade, retains effect-specific gates, correctly retires the Polaris-only transaction, and gives CC-REV-2 an appropriate whole-population ledger requirement.
