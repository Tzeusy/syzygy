REVISE

Two false-green paths remain at exact head `8eadfc6ded77bda945448d1109458b9b21485f54`.

1. High — historical digest validation is file-wide, not quotation-bound. [Observed] Replacing the act-6 CC-SPEC ceremony digest with the later digest and retaining the old digest only in an unrelated HTML comment made the complete governance checker exit 0: CG-7e `12 files / 0 findings`, CG-7h `76 / 0`, total `33 OK / 19 WARN / 0 FAIL`. The cause is [check_governance.py:2086](/home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-general-trusted-bootstrap/scripts/check_governance.py:2086), which accepts `any(d in body)` rather than binding the exact digest to the registered historical quotation grammar. Add per-file/per-label line patterns and a decoy-digest regression fixture.

2. High — simultaneous loss of both performed records re-enables pre-act rewrite mode. [Observed] With both `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md` and `ACCEPTANCE-ACT-RECORD.md` deleted:

   - A post-act coverage mutation made the transaction generator exit 0 and rewrite `ACT-SEMANTICS.md` plus `TRANSACTION-MANIFEST.txt`.
   - A mutated performed impact ledger made the impact generator exit 0 and rewrite the ledger.

   Both `performed_digest` implementations return `None` when both signals are absent at [transaction generator:95](/home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-general-trusted-bootstrap/scripts/build_general_trusted_bootstrap_transaction.py:95) and [impact generator:147](/home/tze/GitHub/syzygy/.worktrees/parallel-agents/syzygy-general-trusted-bootstrap/scripts/build_general_trusted_bootstrap_impact_ledger.py:147). That contradicts the disposition’s claim that the generators require matching signals. The post-act version needs an irreversible performed-state pin, plus both-absent/no-rewrite fixtures.

The four requested direct mutations otherwise passed:

- Fake Wave-A table plus fake quotation: checker exit 1; CG-7d `24 / 1`.
- Later CC-SPEC digest replacing act-6 copy: checker exit 1; CG-7e `12 / 1`.
- Deleting either record individually: both generators exited 1 and every bound output remained byte-identical.
- CRLF-only `ACT-SEMANTICS.md` drift: normalized content matched, digest changed, transaction `--check` exited 1, governance exited 1 with CG-7h `76 / 1`.

Clean-baseline evidence:

- Governance: `33 OK / 19 WARN / 0 FAIL`; CG-7h exactly `76 predicates / 0 findings`.
- Governance selftest: `167 fixtures / 0 failing`.
- Transaction check: frozen/current; selftest `7 mutations / 0 failing`.
- Impact check: frozen/valid, 204 files; selftest `4 mutations / 0 failing`.
- Reviewed worktree remained clean. Temporary clones remain under `/tmp/syzygy-post-act-confirm.0ygQNT` because deletion was blocked by the environment guard.
