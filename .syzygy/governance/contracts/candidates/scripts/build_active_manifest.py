#!/usr/bin/env python3
"""Generate the active-contract manifest and the six wave manifests.

Round-2026-08d replaced the all-in-one act 1 with six independently
acceptable waves (owner work order §4; design record:
`round-2026-08d/ACCEPTANCE-WAVE-DESIGN.md`). Each wave manifest's own
sha256 is that wave act's argument, exactly as the active manifest's
digest was the old act-1 argument.

Rules this script makes executable:

1. **Enumeration is closed and total.** Every `.md` under `rfcs/` is
   assigned to exactly one wave by the tables below; a file the tables do
   not assign is a hard error, never silently included or skipped. A
   non-`.md` file under `rfcs/` is likewise a hard error: adding a module
   and adding it to a wave are one deliberate act.
2. **Digests are scripted, never transcribed; the sort is defined.** Rows
   are `sha256sum`-style, ordered by Python string sort (codepoint order)
   on the repo-relative path — locale-independent, unlike `find | sort`.
3. **The waves partition the package.** The union of the six wave
   manifests equals the active manifest, with no overlap; the partition is
   recomputed and asserted on every run.

Usage:
  build_active_manifest.py            rewrite all seven manifests
  build_active_manifest.py --check    recompute and diff; nonzero on drift
  build_active_manifest.py --selftest mutate a copy, confirm --check fails
  build_active_manifest.py --root D   operate on candidates tree D (tests)
"""
import argparse
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.dirname(HERE)

#: Whole-contract wave membership. RFC-0010/0011 are deliberately absent:
#: their modules split across waves and are assigned per-module below.
WAVE_OF_RFC = {
    "RFC-0001": "A", "RFC-0002": "A", "RFC-0003": "A", "RFC-0004": "A",
    "RFC-0005": "A", "RFC-0006": "A",
    "RFC-0007": "B", "RFC-0008": "B", "RFC-0009": "B",
}
#: Per-module membership for the two split contracts. The package README
#: travels with the first wave that accepts modules of its contract, so the
#: clause map and lookup rule are bound no later than the clauses they map.
WAVE_OF_MODULE = {
    "rfcs/RFC-0011/README.md": "C1",
    "rfcs/RFC-0011/packet-identity-provenance-and-memory.md": "C1",
    "rfcs/RFC-0011/deterministic-selection-and-budget.md": "C2",
    "rfcs/RFC-0010/README.md": "D1",
    "rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md": "D1",
    "rfcs/RFC-0010/prevention-envelope-and-attention.md": "D1",
    "rfcs/RFC-0010/budget-reservation.md": "D1",
    "rfcs/RFC-0010/portfolio-and-cross-project-consent.md": "D1",
    "rfcs/RFC-0010/effects-recovery-and-stop.md": "D2",
}
WAVES = ("A", "B", "C1", "C2", "D1", "D2")
WAVE_TITLE = {
    "A": "kernel, evidence, storage, admission, cross-surface selection "
         "(RFC 0001-0006)",
    "B": "the three surfaces: Polaris, Trajectory, Orrery (RFC 0007-0009)",
    "C1": "context packets: identity, provenance, memory (RFC-0011 module 1"
          " + package index)",
    "C2": "context selection policy and budget posture (RFC-0011 module 2)",
    "D1": "mission control prevention plane (RFC-0010 modules 1-3, 5 "
          "+ package index)",
    "D2": "mission control correction plane (RFC-0010 module 4)",
}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def assign(rel):
    """Wave for one repo-relative rfcs/ path, or an error string."""
    if rel in WAVE_OF_MODULE:
        return WAVE_OF_MODULE[rel], None
    parts = rel.split("/")
    name = parts[1]
    contract = name[:8] if name.startswith("RFC-") else None
    if contract in WAVE_OF_RFC:
        return WAVE_OF_RFC[contract], None
    return None, (f"{rel} — not assigned to any wave; assign it in "
                  f"build_active_manifest.py deliberately")


def enumerate_modules(root):
    errors, assigned = [], {}
    rfcs = os.path.join(root, "rfcs")
    for dirpath, dirs, names in os.walk(rfcs):
        dirs.sort()
        for n in sorted(names):
            rel = os.path.relpath(os.path.join(dirpath, n), root).replace(
                os.sep, "/")
            if not n.endswith(".md"):
                errors.append(f"{rel} — non-.md file under rfcs/; remove it "
                              f"or teach the generator about it deliberately")
                continue
            wave, err = assign(rel)
            if err:
                errors.append(err)
            else:
                assigned[rel] = wave
    return dict(sorted(assigned.items())), errors


def manifest_text(rows, header_lines):
    out = [f"# {ln}" for ln in header_lines]
    out += [f"{sha}  {rel}" for rel, sha in rows]
    return "\n".join(out) + "\n"


def build(root):
    assigned, errors = enumerate_modules(root)
    if errors:
        return None, errors
    per_wave = {w: [] for w in WAVES}
    all_rows = []
    for rel in sorted(assigned):
        sha = sha256_file(os.path.join(root, rel))
        all_rows.append((rel, sha))
        per_wave[assigned[rel]].append((rel, sha))
    # Partition invariants — recomputed, never assumed.
    union = sorted(r for w in WAVES for r, _ in per_wave[w])
    if union != sorted(assigned):
        return None, ["wave partition does not equal the active set — "
                      "generator defect, refuse to write"]
    empty = [w for w in WAVES if not per_wave[w]]
    if empty:
        return None, [f"wave {w} is empty — a wave act with no subject is "
                      f"an error" for w in empty]
    files = {}
    files["ACTIVE-CONTRACT-MANIFEST.txt"] = manifest_text(all_rows, [
        "ACTIVE-CONTRACT-MANIFEST — final pre-specification package "
        "(round-2026-08d wave structure)",
        f"sha256 per active module, {len(all_rows)} modules; rows sorted by "
        "codepoint order of the path.",
        "Generated by scripts/build_active_manifest.py — regenerate with it; "
        "never hand-edit.",
        "The six wave manifests in wave-manifests/ partition this set; each "
        "wave manifest's own sha256 is that wave act's argument "
        "(FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md).",
    ])
    for w in WAVES:
        files[f"wave-manifests/WAVE-{w}-MANIFEST.txt"] = manifest_text(
            per_wave[w], [
                f"WAVE-{w}-MANIFEST — {WAVE_TITLE[w]}",
                f"{len(per_wave[w])} module(s); subset of "
                "ACTIVE-CONTRACT-MANIFEST.txt; rows sorted by codepoint "
                "order of the path.",
                "Generated by scripts/build_active_manifest.py — regenerate "
                "with it; never hand-edit.",
                f"This file's own sha256 is the argument of the phrase "
                f"`ACCEPT FOUNDATIONAL WAVE {w}: <sha256>`.",
            ])
    return files, []


def run(root, check):
    files, errors = build(root)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 2
    drift = []
    for rel, content in files.items():
        path = os.path.join(root, rel)
        existing = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                existing = fh.read()
        if existing != content:
            drift.append(rel)
            if not check:
                os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(content)
    if check:
        for d in drift:
            print(f"DRIFT: {d} — differs from regeneration")
        if drift:
            return 1
        print(f"all {len(files)} manifests match regeneration")
        return 0
    for rel in files:
        sha = hashlib.sha256(files[rel].encode()).hexdigest()
        print(f"{'rewrote' if rel in drift else 'unchanged'}  {rel}  "
              f"sha256 {sha}")
    return 0


def selftest(root):
    """Mutate a copy of the tree per failure class; confirm --check fails.

    Verification rule 6: a check nobody has seen fail is not evidence.
    """
    import shutil
    import tempfile
    ok = True
    cases = []

    def clone():
        d = tempfile.mkdtemp(prefix="manifest-selftest-")
        shutil.copytree(os.path.join(root, "rfcs"), os.path.join(d, "rfcs"))
        rc = run(d, check=False)
        assert rc == 0, "selftest setup: clean generation failed"
        return d

    # 1. Module content mutated → active + wave manifests both drift.
    d = clone()
    target = os.path.join(d, "rfcs/RFC-0010/effects-recovery-and-stop.md")
    with open(target, "a", encoding="utf-8") as fh:
        fh.write("\nmutation\n")
    cases.append(("module content mutation detected", run(d, check=True) != 0))
    shutil.rmtree(d)

    # 2. Unassigned module added → hard error, not silent inclusion.
    d = clone()
    with open(os.path.join(d, "rfcs/RFC-9999-unassigned.md"), "w") as fh:
        fh.write("stray\n")
    cases.append(("unassigned module rejected", run(d, check=True) == 2))
    shutil.rmtree(d)

    # 3. Non-.md file under rfcs/ → hard error.
    d = clone()
    with open(os.path.join(d, "rfcs/RFC-0010/notes.txt"), "w") as fh:
        fh.write("stray\n")
    cases.append(("non-.md file rejected", run(d, check=True) == 2))
    shutil.rmtree(d)

    # 4. Hand-edited wave manifest → drift.
    d = clone()
    wm = os.path.join(d, "wave-manifests/WAVE-A-MANIFEST.txt")
    with open(wm, "a", encoding="utf-8") as fh:
        fh.write("0" * 64 + "  rfcs/forged.md\n")
    cases.append(("hand-edited wave manifest detected",
                  run(d, check=True) != 0))
    shutil.rmtree(d)

    for label, passed in cases:
        print(f"SELFTEST {'OK' if passed else 'FAIL'}: {label}")
        ok = ok and passed
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--root", default=DEFAULT_ROOT)
    args = ap.parse_args()
    if args.selftest:
        sys.exit(selftest(args.root))
    sys.exit(run(args.root, args.check))
