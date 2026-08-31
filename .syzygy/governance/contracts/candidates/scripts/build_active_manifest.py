#!/usr/bin/env python3
"""Maintain the current manifest and the six wave-manifest act arguments.

Round-2026-08d replaced the all-in-one act 1 with six independently
acceptable waves (owner work order §4; design record:
`round-2026-08d/ACCEPTANCE-WAVE-DESIGN.md`). Each wave manifest's own
sha256 is that wave act's argument, exactly as the active manifest's
digest was the old act-1 argument.

A performed wave manifest is an immutable historical act argument. Its rows
retain the module digests accepted at the act even when a later, separately
authorized amendment changes those modules. This script verifies the
performed manifest's own digest against `decisions/ACCEPTANCE-ACT-RECORD.md`
and verifies that its paths still equal the wave's current path membership;
it never rewrites the performed bytes. `ACTIVE-CONTRACT-MANIFEST.txt` and
unperformed wave manifests continue to track current candidate bytes. A
current amendment is bound by its own amendment manifest, never by rewriting
the historical wave argument.

Rules this script makes executable:

1. **Enumeration is closed and total.** Every `.md` under `rfcs/` is
   assigned to exactly one wave by the tables below; a file the tables do
   not assign is a hard error, never silently included or skipped. A
   non-`.md` file under `rfcs/` is likewise a hard error: adding a module
   and adding it to a wave are one deliberate act.
2. **Digests are scripted, never transcribed; the sort is defined.** Rows
   are `sha256sum`-style, ordered by Python string sort (codepoint order)
   on the repo-relative path — locale-independent, unlike `find | sort`.
3. **The waves partition the package by path.** The union of the six wave
   manifest path sets equals the active manifest path set, with no overlap;
   the partition is recomputed and asserted on every run. Row digests in a
   performed manifest are act-time history, not current-byte assertions.

Usage:
  build_active_manifest.py            rewrite current manifests; preserve acts
  build_active_manifest.py --check    verify current and performed manifests
  build_active_manifest.py --selftest mutate a copy, confirm --check fails
  build_active_manifest.py --root D   operate on candidates tree D (tests)
"""
import argparse
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.dirname(HERE)

#: Whole-contract wave membership, for **packaged** contracts only — a
#: `rfcs/RFC-00nn/` directory. RFC-0010/0011 are deliberately absent: their
#: modules split across waves and are assigned per-module below.
#:
#: This table never assigns a *top-level* `rfcs/*.md` file. Review RD-17
#: finding 8: `assign()` took `name[:8]` of any file starting with `RFC-`, so
#: a stray `rfcs/RFC-0006-scratch.md` was silently admitted to Wave A — the
#: owner's act argument — against the docstring rule directly above, which
#: says an unassigned file is a hard error. The generator's own selftest used
#: `RFC-9999-unassigned.md`, a name whose prefix collides with nothing, so
#: the fixture passed on the one input shape that could not exercise the hole.
WAVE_OF_RFC = {
    "RFC-0001": "A", "RFC-0002": "A", "RFC-0003": "A", "RFC-0004": "A",
    "RFC-0005": "A", "RFC-0006": "A",
    "RFC-0007": "B", "RFC-0008": "B", "RFC-0009": "B",
}
#: Per-module membership: every top-level single-file contract by exact name,
#: and the split contracts' modules. The package README travels with the
#: first wave that accepts modules of its contract, so the clause map and
#: lookup rule are bound no later than the clauses they map.
WAVE_OF_MODULE = {
    "rfcs/RFC-0001-project-graph-identity-state-planes.md": "A",
    "rfcs/RFC-0006-cross-surface-selection-query-drawer.md": "A",
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
PERFORMED_WAVES_REQUIRED = ("A", "B")
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

ACT_ARGUMENT_RE = re.compile(
    r"^ACCEPT FOUNDATIONAL WAVE (A|B|C1|C2|D1|D2): "
    r"([0-9a-f]{64})$", re.MULTILINE)
DIGEST_ROW = re.compile(r"^(?P<sha>[0-9a-f]{64})  (?P<path>rfcs/\S+)$")


def default_act_record(root):
    """Performed-act record paired with a candidates root."""
    return os.path.normpath(os.path.join(
        root, "..", "..", "decisions", "ACCEPTANCE-ACT-RECORD.md"))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def performed_wave_arguments(act_record):
    """Return performed wave -> immutable manifest digest from the act record.

    The performed record, not the still-editable offering record and not a
    constant in this generator, owns the historical argument.
    """
    try:
        with open(act_record, encoding="utf-8") as fh:
            body = fh.read()
    except OSError as exc:
        return None, [f"{act_record} — performed-act record unreadable: {exc}"]
    found = {}
    errors = []
    for wave, digest in ACT_ARGUMENT_RE.findall(body):
        if wave in found:
            errors.append(
                f"{act_record} — performed Wave {wave} phrase occurs more "
                "than once; the immutable act argument is ambiguous")
        else:
            found[wave] = digest
    for wave in PERFORMED_WAVES_REQUIRED:
        if wave not in found:
            errors.append(
                f"{act_record} — performed Wave {wave} act argument missing")
    return (found if not errors else None), errors


def manifest_rows(path, display):
    """Parse one manifest strictly, returning ordered `(path, digest)` rows."""
    rows, errors = [], []
    try:
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
    except OSError as exc:
        return None, [f"{display} — manifest unreadable: {exc}"]
    for line_no, line in enumerate(lines, 1):
        if not line or line.startswith("#"):
            continue
        match = DIGEST_ROW.fullmatch(line)
        if not match:
            errors.append(
                f"{display}:{line_no} — malformed manifest row; expected "
                "`<64 lowercase hex><two spaces><rfcs/path>`")
            continue
        rows.append((match.group("path"), match.group("sha")))
    paths = [rel for rel, _sha in rows]
    if len(paths) != len(set(paths)):
        errors.append(f"{display} — duplicate module path in manifest")
    if paths != sorted(paths):
        errors.append(
            f"{display} — rows are not in codepoint path order")
    if not rows:
        errors.append(f"{display} — manifest has no module rows")
    return (rows if not errors else None), errors


def validate_performed_manifests(root, per_wave, act_record):
    """Validate immutable act arguments without re-hashing historical rows.

    The manifest's own recorded digest proves its bytes are the act-time
    bytes. Only row *paths* are compared with today's wave assignment. Row
    digests deliberately remain the content digests accepted at the act.
    """
    arguments, errors = performed_wave_arguments(act_record)
    if errors:
        return None, errors
    for wave, recorded_digest in sorted(arguments.items()):
        rel = f"wave-manifests/WAVE-{wave}-MANIFEST.txt"
        full = os.path.join(root, rel)
        if not os.path.exists(full):
            errors.append(
                f"{rel} — performed Wave {wave} manifest is missing")
            continue
        actual_digest = sha256_file(full)
        if actual_digest != recorded_digest:
            errors.append(
                f"{rel} — sha256 {actual_digest} does not equal performed "
                f"act argument {recorded_digest}; refuse to rewrite history")
            continue
        rows, row_errors = manifest_rows(full, rel)
        errors.extend(row_errors)
        if rows is None:
            continue
        actual_paths = [path for path, _sha in rows]
        expected_paths = [path for path, _sha in per_wave[wave]]
        if actual_paths != expected_paths:
            missing = sorted(set(expected_paths) - set(actual_paths))
            extra = sorted(set(actual_paths) - set(expected_paths))
            errors.append(
                f"{rel} — performed manifest path membership differs from "
                f"current Wave {wave} assignment; missing={missing}, "
                f"unexpected={extra}")
    return (arguments if not errors else None), errors


def declaring_waves(rel):
    """Every wave table that claims this module — **no precedence applied**.

    `assign()` below resolves a double claim by letting the module table win,
    which is the right behaviour for generating and the wrong behaviour for
    *checking*: it hides the very disagreement the partition assertion is
    supposed to find. This function is the second, precedence-free reading
    that `build()` asserts against, so adding (say) `"RFC-0011": "A"` to
    `WAVE_OF_RFC` is a hard error instead of a silent reassignment.

    A top-level `rfcs/*.md` is claimed **only by exact name**. Directory
    membership is claimed only for `rfcs/RFC-00nn/…` paths.
    """
    out = []
    if rel in WAVE_OF_MODULE:
        out.append(WAVE_OF_MODULE[rel])
    parts = rel.split("/")
    if len(parts) > 2 and parts[1] in WAVE_OF_RFC:
        out.append(WAVE_OF_RFC[parts[1]])
    return out


def assign(rel):
    """Wave for one repo-relative rfcs/ path, or an error string.

    **The generating rule**, and it applies precedence: a module named
    outright wins over its contract's directory membership. `build()` asserts
    this against `declaring_waves()`, which applies none — two readings, so
    the partition assertion has something to be false about.

    A top-level `rfcs/*.md` resolves **only** by exact name. The prefix match
    that used to stand here (`name[:8]`) admitted `RFC-0006-scratch.md` to
    Wave A without a word (review RD-17 finding 8).
    """
    if rel in WAVE_OF_MODULE:
        return WAVE_OF_MODULE[rel], None
    parts = rel.split("/")
    if len(parts) > 2 and parts[1] in WAVE_OF_RFC:
        return WAVE_OF_RFC[parts[1]], None
    return None, (f"{rel} — not assigned to any wave; assign it in "
                  f"build_active_manifest.py deliberately. A top-level "
                  f"`rfcs/*.md` needs an exact `WAVE_OF_MODULE` entry: a "
                  f"prefix match once admitted a stray file to Wave A")


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


def build(root, act_record):
    assigned, errors = enumerate_modules(root)
    if errors:
        return None, errors
    all_rows = []
    for rel in sorted(assigned):
        all_rows.append((rel, sha256_file(os.path.join(root, rel))))

    # **The partition, recomputed from a second and independent reading.**
    # `per_wave` used to be filled by iterating `assigned` — so
    # `union == sorted(assigned)` held by construction and the assertion
    # could not fail. Review RD-17 finding 9 proved it: the only way the old
    # comparison could differ was a wave label outside `WAVES`, and that path
    # raised `KeyError` before reaching the assert. The real partition
    # coverage lived in `check_governance.py` CG-7a, not here, while this
    # docstring claimed it.
    #
    # The second reading is `declaring_waves()`, which applies no precedence.
    # It can and does disagree with `assign()` — whenever two tables claim
    # one module — which is what makes the assertion a check.
    per_wave = {w: [] for w in WAVES}
    disagreements = []
    for rel, sha in all_rows:
        claims = declaring_waves(rel)
        if len(claims) != 1:
            disagreements.append(
                f"{rel} — the wave tables claim it {len(claims)} time(s) "
                f"({sorted(set(claims)) or 'not at all'}); the partition "
                f"assertion is recomputed without precedence, and precedence "
                f"is exactly what would hide this")
            continue
        if claims[0] != assigned[rel]:
            disagreements.append(
                f"{rel} — assigned to wave {assigned[rel]} but the tables "
                f"read without precedence give {claims[0]}")
            continue
        per_wave[claims[0]].append((rel, sha))
    if disagreements:
        return None, disagreements
    union = sorted(r for w in WAVES for r, _ in per_wave[w])
    if union != sorted(assigned):
        return None, ["wave partition does not equal the active set — "
                      "generator defect, refuse to write"]
    empty = [w for w in WAVES if not per_wave[w]]
    if empty:
        return None, [f"wave {w} is empty — a wave act with no subject is "
                      f"an error" for w in empty]
    performed, performed_errors = validate_performed_manifests(
        root, per_wave, act_record)
    if performed_errors:
        return None, performed_errors
    files = {}
    files["ACTIVE-CONTRACT-MANIFEST.txt"] = manifest_text(all_rows, [
        "ACTIVE-CONTRACT-MANIFEST — current candidate contract bytes "
        "(round-2026-08d wave path structure)",
        f"sha256 per active module, {len(all_rows)} modules; rows sorted by "
        "codepoint order of the path.",
        "Generated by scripts/build_active_manifest.py — regenerate with it; "
        "never hand-edit.",
        "The six wave manifests partition this set by path. Performed wave "
        "manifests preserve act-time content digests; unperformed wave "
        "manifests track current candidate bytes.",
        "Current amendments use a separate amendment manifest; they never "
        "rewrite a performed wave manifest or its recorded act argument.",
    ])
    for w in WAVES:
        if w in performed:
            continue
        files[f"wave-manifests/WAVE-{w}-MANIFEST.txt"] = manifest_text(
            per_wave[w], [
                f"WAVE-{w}-MANIFEST — {WAVE_TITLE[w]}",
                f"{len(per_wave[w])} module(s); subset of "
                "ACTIVE-CONTRACT-MANIFEST.txt; rows sorted by codepoint "
                "order of the path.",
                "Generated while this wave is unperformed; after a recorded "
                "owner act, these exact bytes become immutable history.",
                f"While unperformed, this file's current sha256 is the "
                f"offered argument of `ACCEPT FOUNDATIONAL WAVE {w}: "
                "<sha256>`.",
            ])
    return (files, performed), []


def stray_wave_manifests(root):
    """Files outside the closed six-manifest wave population.

    Review RD-17 finding 5: the directory was never a population. A seventh,
    internally false `WAVE-C-MANIFEST.txt` dropped into it produced *all 7
    manifests match regeneration* from this script and zero findings from the
    whole battery — in the one directory the acceptance record sends an owner
    to for each wave act's argument.
    """
    home = os.path.join(root, "wave-manifests")
    if not os.path.isdir(home):
        return []
    expected = {f"WAVE-{wave}-MANIFEST.txt" for wave in WAVES}
    return sorted(f"wave-manifests/{n} — sits in the wave-manifest home and "
                  f"is not one of the {len(expected)} manifests this script "
                  f"maintains or preserves; a file here reads as a wave "
                  f"act's argument"
                  for n in os.listdir(home)
                  if os.path.isfile(os.path.join(home, n))
                  and n not in expected)


def run(root, check, act_record=None):
    act_record = act_record or default_act_record(root)
    built, errors = build(root, act_record)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 2
    files, performed = built
    strays = stray_wave_manifests(root)
    if strays:
        for s in strays:
            print(f"ERROR: {s}")
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
        # The denominator, every run. "no drift" over an unstated population
        # is the shape `check_governance.py` refuses in its own output, and
        # review RD-17 finding 13 noted this script's `--check` line stated
        # none: a corpus that lost half its modules would regenerate to a
        # smaller manifest and still print agreement.
        n_modules = sum(1 for ln in files["ACTIVE-CONTRACT-MANIFEST.txt"]
                        .splitlines() if not ln.startswith("#"))
        pop = (f"{len(files)} current manifest(s) regenerated over "
               f"{n_modules} module(s), {len(performed)} performed wave "
               f"manifest(s) preserved, {len(WAVES)} wave path sets checked")
        if drift:
            print(f"population: {pop}")
            return 1
        print("current manifests match regeneration and performed wave "
              f"arguments verify — {pop}")
        return 0
    for rel in files:
        sha = hashlib.sha256(files[rel].encode()).hexdigest()
        print(f"{'rewrote' if rel in drift else 'unchanged'}  {rel}  "
              f"sha256 {sha}")
    for wave, digest in sorted(performed.items()):
        print(f"preserved  wave-manifests/WAVE-{wave}-MANIFEST.txt  "
              f"performed-act sha256 {digest}")
    return 0


def selftest(root, act_record=None):
    """Mutate a copy of the tree per failure class; confirm --check fails.

    Verification rule 6: a check nobody has seen fail is not evidence.
    """
    import shutil
    import tempfile
    ok = True
    cases = []
    act_record = act_record or default_act_record(root)
    performed, argument_errors = performed_wave_arguments(act_record)
    assert not argument_errors, (
        "selftest setup: performed act arguments unavailable: "
        + "; ".join(argument_errors))

    def clone():
        d = tempfile.mkdtemp(prefix="manifest-selftest-")
        shutil.copytree(os.path.join(root, "rfcs"), os.path.join(d, "rfcs"))
        os.makedirs(os.path.join(d, "wave-manifests"))
        for wave in performed:
            shutil.copy2(
                os.path.join(root, f"wave-manifests/WAVE-{wave}-MANIFEST.txt"),
                os.path.join(d, f"wave-manifests/WAVE-{wave}-MANIFEST.txt"))
        rc = run(d, check=False, act_record=act_record)
        assert rc == 0, "selftest setup: clean generation failed"
        return d

    # 1. A performed-wave module changes under a later amendment. Regeneration
    # updates the active manifest but preserves the historical act argument.
    d = clone()
    target_rel = "rfcs/RFC-0002/challenge-lifecycle.md"
    target = os.path.join(d, target_rel)
    wave_a = os.path.join(d, "wave-manifests/WAVE-A-MANIFEST.txt")
    before = sha256_file(wave_a)
    with open(target, "a", encoding="utf-8") as fh:
        fh.write("\nperformed-wave amendment\n")
    rc = run(d, check=False, act_record=act_record)
    active_rows, active_errors = manifest_rows(
        os.path.join(d, "ACTIVE-CONTRACT-MANIFEST.txt"),
        "ACTIVE-CONTRACT-MANIFEST.txt")
    current = dict(active_rows or []).get(target_rel)
    cases.append((
        "performed-wave amendment updates active without rewriting act manifest",
        rc == 0 and not active_errors and before == sha256_file(wave_a)
        and before == performed["A"] and current == sha256_file(target)
        and run(d, check=True, act_record=act_record) == 0))
    shutil.rmtree(d)

    # 1b. An unperformed-wave module mutation still drifts both current
    # manifests until regeneration.
    d = clone()
    target = os.path.join(d, "rfcs/RFC-0010/effects-recovery-and-stop.md")
    with open(target, "a", encoding="utf-8") as fh:
        fh.write("\nmutation\n")
    cases.append(("unperformed module content mutation detected",
                  run(d, check=True, act_record=act_record) == 1))
    shutil.rmtree(d)

    # 2. Unassigned module added → hard error, not silent inclusion.
    d = clone()
    with open(os.path.join(d, "rfcs/RFC-9999-unassigned.md"), "w") as fh:
        fh.write("stray\n")
    cases.append(("unassigned module rejected",
                  run(d, check=True, act_record=act_record) == 2))
    shutil.rmtree(d)

    # 2b. **The colliding name.** Case 2's `RFC-9999` collides with no wave
    # table entry, so it passed on the one input shape that could not
    # exercise the prefix match review RD-17 finding 8 found: `name[:8]` of
    # `RFC-0006-scratch.md` is `RFC-0006`, which `WAVE_OF_RFC` claimed, and
    # the stray entered Wave A silently — the owner's act argument, enlarged
    # by a regeneration nobody would read as an assignment.
    d = clone()
    with open(os.path.join(d, "rfcs/RFC-0006-scratch.md"), "w") as fh:
        fh.write("stray\n")
    rc = run(d, check=True, act_record=act_record)
    assigned_now, errs = enumerate_modules(d)
    cases.append(("colliding stray name rejected, not admitted to Wave A",
                  rc == 2 and "rfcs/RFC-0006-scratch.md" not in assigned_now
                  and any("RFC-0006-scratch" in e for e in errs)))
    shutil.rmtree(d)

    # 2c. The partition assertion, made falsifiable. Two tables claiming one
    # module used to be resolved by precedence and never reported; the
    # precedence-free second reading in `build()` is what catches it.
    d = clone()
    saved = dict(WAVE_OF_RFC)
    WAVE_OF_RFC["RFC-0011"] = "A"
    try:
        _files, errs = build(d, act_record)
        cases.append(("double-claimed module fails the partition assertion",
                      _files is None
                      and any("claim it 2 time(s)" in e for e in errs)))
    finally:
        WAVE_OF_RFC.clear()
        WAVE_OF_RFC.update(saved)
    shutil.rmtree(d)

    # 5. A seventh file in `wave-manifests/` — the directory the acceptance
    # record sends an owner to — used to be invisible to this script and to
    # the whole battery (review RD-17 finding 5).
    d = clone()
    with open(os.path.join(d, "wave-manifests/WAVE-C-MANIFEST.txt"), "w") as fh:
        fh.write("0" * 64 + "  rfcs/forged.md\n")
    cases.append(("stray file in wave-manifests/ rejected",
                  run(d, check=True, act_record=act_record) == 2))
    shutil.rmtree(d)

    # 3. Non-.md file under rfcs/ → hard error.
    d = clone()
    with open(os.path.join(d, "rfcs/RFC-0010/notes.txt"), "w") as fh:
        fh.write("stray\n")
    cases.append(("non-.md file rejected",
                  run(d, check=True, act_record=act_record) == 2))
    shutil.rmtree(d)

    # 4. Tampering a performed manifest is an act-argument failure. The
    # generator refuses to rewrite it even in write mode.
    d = clone()
    wm = os.path.join(d, "wave-manifests/WAVE-A-MANIFEST.txt")
    with open(wm, "a", encoding="utf-8") as fh:
        fh.write("0" * 64 + "  rfcs/forged.md\n")
    cases.append(("tampered performed manifest rejected",
                  run(d, check=True, act_record=act_record) == 2
                  and sha256_file(wm) != performed["A"]))
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
    ap.add_argument("--act-record", default=None,
                    help="performed ACCEPTANCE-ACT-RECORD.md paired with "
                         "--root (defaults to the repository location)")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(selftest(args.root, args.act_record))
    sys.exit(run(args.root, args.check, args.act_record))
