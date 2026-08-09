# Topology bundle manifest

**Purpose:** the single digest-bearing identity for the topology bundle.
The owner act `ACCEPT TOPOLOGY: <digest-of-this-file>` accepts exactly the
nine files below at exactly these content digests (RFC3-16: the act binds
this manifest's own sha256; the manifest binds each member file). Editing
any member file invalidates this manifest; a regenerated manifest has a new
digest and needs a new act.
**Date:** 2026-08-02 (rev8 rework, directive items 1 and 9); member digests regenerated 2026-08-05 (P-6 second leg) and again 2026-08-10 after the second retired-acceptance-phrase correction in README.md (the recurred rev10-phrase defect, launch-gate pilot C1; the sentence is now phrase-free so the class cannot recur here; semantic delta on record).

## Member files (sha256)

```
b081089317f476d9e33b669a4ef41fa659dfc32fccb628ada5efc4cc666fa009  01-system-context.md
6e0c75afb915fd07cc70d80d0515834cf04d33c475daba23f0188057a4bca90d  02-project-workspace-repos.md
50e48478b352f7864f1dbc201dbe1fcd3d1aa847cb6a4cc791300796d0446178  03-kernel-and-surfaces.md
a9aff9170547863be863b0bb4e80c8d34baaad13e855fdc22104e561aaf96590  04-authority-write-boundaries.md
27a9b38d9d34d60ad06feb2542a45b81e95840f35406a9d026710633e77f716f  05-observation-evidence-flow.md
d6712766e58842244c67e9d3e50fca94fd9c59ff838f1b6f6f6cc876e4d6b8ca  06-intent-to-reconciliation-flow.md
0f6e903a1c72ef1cd6dca906ef5a7d7b04e92a18db0f6d82c2e67cc0fd5947ec  07-client-trust-boundaries.md
21768048fce64d7f33ff4a4bf9d1e72ed0954c7c359db0aaaf2aba4b7ea700b4  08-adapter-external-systems.md
a0621a0d20669d25b4382aff0dcfe227d85811cfd4348db211e780c0e6cf7d14  README.md
```

Verify anytime with `sha256sum -c` against this block (from `topology/`).
