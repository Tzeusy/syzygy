REVISE

1. High — arbitrary table rows can forge performed-history digests. `scripts/check_governance.py:1816-1857` treats any table row containing an act subject’s basename and one backticked digest as performed, without tying it to a recognized act type or transaction section. A mutation adding a fake `WAVE-A-MANIFEST.txt` row plus an unmarked fake Wave-A quotation exited 0: CG-7d reported 24 quotations/0 findings, CG-7e 12 files/0 findings, and CG-7h 76 predicates/0 findings. This violates fail-closed history handling.

2. High — historical copies are bound only to an act label, not their specific act-time digest. `scripts/check_governance.py:1970-1983` registers historical files by label, while `:2061-2070` accepts any performed digest for that label. Replacing the 2026-08-17 CC-SPEC digest in `SPECIFICATION-ACCEPTANCE-DECISION.md:41` with the 2026-09-01 digest still exited 0 and was reported by CG-7e as “1 historical valid.” Historical entries need an exact act-entry/digest binding.

3. High — deleting the dedicated act file disables both post-act freeze guards despite the append-only acceptance record still proving performance. `build_general_trusted_bootstrap_transaction.py:80-89,238-301` and `build_general_trusted_bootstrap_impact_ledger.py:132-141,368-403` treat the absent dedicated record as pre-act state. Mutation results:

   - Transaction builder exited 0 and rewrote `ACT-SEMANTICS.md` and `TRANSACTION-MANIFEST.txt` after the dedicated act file was removed.
   - Impact builder exited 0 and rewrote the bound ledger from `4144b849…` to `35e6669c…`.

   Both builders should consult both performed records and fail closed on a missing or conflicting post-act signal.

4. Medium — transaction generated-subject comparison is text-normalized, not byte-exact. `build_general_trusted_bootstrap_transaction.py:245-249` uses `read_text() != content`. Converting only `ACT-SEMANTICS.md` to CRLF changed its digest, yet `--check` exited 0 and claimed the performed transaction was “frozen and current.” CG-7h correctly failed on the digest mismatch. Compare `read_bytes()` against `content.encode()`.

Verified strengths:

- Detached clone at exact `dc3797468508f0193b3e0eaf4203aa846247d800`.
- Baseline checker: 806 files, exit 0; CG-7h exactly `4 + 7 + 30 + 5 + 30 = 76`, zero findings.
- Manifest counts independently reproduced as 7/30/5; all rows passed `sha256sum -c`; 30/30 installed/candidate mirrors matched.
- `--selftest`: 165 fixtures, 0 failing. Transaction and impact freeze selftests passed.
- Missing top-level row failed with 75 predicates and three findings. Mirror divergence failed CG-7h at 76 predicates. Existing fixtures detect missing/mismatched acts and top-level, nested-contract, and nested-PWB drift.
- Historical Wave A/B manifests still hash to `8972d963…` and `193e3c…`; the 2026-08-17 tag retains CC-SPEC `9889b7e3…`, while current CC-SPEC is `6093dbbe…`. The bytes remain recoverable, but finding 2 shows the checker does not enforce that exact historical association.

No shared-checkout files were edited; all mutation probes ran in disposable detached clones.
