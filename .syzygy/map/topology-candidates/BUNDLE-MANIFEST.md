# Topology bundle manifest

**Purpose:** the single digest-bearing identity for the topology bundle.
The owner act `ACCEPT TOPOLOGY: <digest-of-this-file>` accepts exactly the
nine files below at exactly these content digests (RFC3-16: the act binds
this manifest's own sha256; the manifest binds each member file). Editing
any member file invalidates this manifest; a regenerated manifest has a new
digest and needs a new act.
**Date:** 2026-08-02 (rev8 rework, directive items 1 and 9); member digests regenerated 2026-08-05 (P-6 second leg) and again 2026-08-10 after the second retired-acceptance-phrase correction in README.md (the recurred rev10-phrase defect, launch-gate pilot C1; the sentence is now phrase-free so the class cannot recur here; semantic delta on record), and again 2026-09-28 after the tree-style readability restyle (no change of meaning).

## Member files (sha256)

```
80fad1dc253e68c2c1334b12a89a6d1e89cd98c00e391af0efd52f6e1b0c6970  01-system-context.md
950337ece16a3ece55f5d2007c48ed1c9161f52bc06e177b1973bd4e39c7ed43  02-project-workspace-repos.md
2d227b1083804f53e18d8e1f47a59b0660a8817c0f0540c12d132be76e3084ed  03-kernel-and-surfaces.md
61043b7b1239847cb0de043a88280a6ff8e5256618d6ae09bd7c17f391ac78d7  04-authority-write-boundaries.md
cba90be8dbbc42930431c34b34f60d03ad712adc1e8b6ef45980e854e21d95e1  05-observation-evidence-flow.md
0c5777251f5c2b67c876c6b436b181118c648868a9be33742956628e4ab3e866  06-intent-to-reconciliation-flow.md
43213324ef692795b64ee2df5a17d2c8654c071cf52e69596431b399790ca49c  07-client-trust-boundaries.md
9068f1e353b5e1a398d74c946ddf1d2fdb0f80da784a7520b9e8af75c8576f2b  08-adapter-external-systems.md
d1a11ce7637ad633ac04e6f53aeece102b28e20b11bb729cf01802ed236e9449  README.md
```

Verify anytime with `sha256sum -c` against this block — run it from
`topology-candidates/` (this directory); `topology/` exists only after
act 3 installs the bundle, and running it there is the post-act check.
