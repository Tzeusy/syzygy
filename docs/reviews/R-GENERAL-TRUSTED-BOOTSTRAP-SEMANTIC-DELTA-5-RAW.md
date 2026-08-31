**CONFIRM**

Bound to sha256 `a577ce1d4509e09c3ef76b7277d7e4186f0750f7ae7299385de5b57a7fbe99f3`.

The added consumers are correct:

- RFC3-2/15 keep sweep outputs kernel-recorded facts; only the resolving policy carries the effective owner act.
- RFC4-12 applies effective-act provenance to the secret policy, not observed facts.
- RFC4-26 applies it to marker-adoption policy while markers remain untrusted.
- RFC9-8(a) correctly treats the portfolio registry as authorization-bearing.
- No evidence or kernel record is converted into an owner act.

The explicit contradiction set is now complete enough to implement, subject to the separately generated whole-corpus impact ledger and normal CC-REV-2 verification.
