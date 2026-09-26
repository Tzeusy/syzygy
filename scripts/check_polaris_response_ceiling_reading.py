#!/usr/bin/env python3
"""Check the response-ceiling reading packet (syzygy-dov.27, P-77 Q2).

The packet is a plain owner-direction offering: it binds no digest, so
there is no manifest to build. What can drift is what it quotes and what it
covers. This script checks, read-only:

  C1 every quoted clause is present, whitespace-normalized, both in its
     source file and in the packet;
  C2 the packet names every response ceiling whose registry sentence opens
     "the final encoded HTTP body", in the registry as it stands and as the
     candidate .18 patch would leave it;
  C3 while no issued direction exists, no non-test TypeScript source under
     apps/*/src or packages/*/src carries compression code (a sweep over
     zero files fails);
  C4 the packet keeps its candidate banner, an open-questions section in
     which every question states a default, and no 64-hex digest;
  C5 every candidate patch under contracts/candidates/*/proposed/ that
     targets a quoted file, applied alone, leaves every quote from that
     file intact.

--selftest breaks each predicate in a scratch fixture and confirms failure.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DECISIONS = ".syzygy/governance/decisions"
PACKET = f"{DECISIONS}/POLARIS-RESPONSE-CEILING-READING-DECISION-PACKET.md"
DIRECTION = f"{DECISIONS}/POLARIS-RESPONSE-CEILING-READING-DIRECTION.md"
REGISTRY = ".syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json"
CANDIDATES = ".syzygy/governance/contracts/candidates"
BRIEFING_PATCH = f"{CANDIDATES}/pwb-registry-currency-briefing-amendment/proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch"
RULINGS = f"{DECISIONS}/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md"
CONTINUATION = f"{DECISIONS}/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md"
RETENTION = f"{DECISIONS}/POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md"
ROUTES = "apps/three-surface-poc/src/routes.ts"
SPEC = "openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md"
VISION = ".syzygy/governance/doctrine/vision.md"

CEILING_PREFIX = "the final encoded HTTP body"
IN_FORCE_CEILINGS = ("maxHumanResponseBytes", "maxMachineResponseBytes")

QUOTES: tuple[tuple[str, str, str], ...] = (
    ("P-77 Q2 ruling", RULINGS, "Q2 compression needs a dated owner act on the ceiling reading before it ships"),
    ("P-77 registry consequence", RULINGS, "The registry entry is edited on no arm."),
    ("P-79 Q1 ruling", RULINGS, "a retention-posture change needing an owner act before slice 1"),
    ("continuation trigger", CONTINUATION, "a change to the constraints or envelope the 2026-09-05 registry entry declares"),
    ("retention direction shape", RETENTION, "binds no artifact digest, needs no manifest or recorder script"),
    ("human ceiling sentence", REGISTRY, "the final encoded HTTP body for each Polaris HTML response"),
    ("machine ceiling sentence", REGISTRY, "the final encoded HTTP body for each authenticated Polaris machine JSON response"),
    ("final-output breach rule", REGISTRY, "final-output breaches emit only a bounded typed failure carrying evaluation identity, limit identity, declared value, observed value and population counts; no truncated or success-shaped model is emitted"),
    ("measurement line", ROUTES, "const observed = Buffer.byteLength(body, 'utf8');"),
    ("PWB-REQ-006 ceiling sentence", SPEC, "Final encoded human HTML and machine JSON SHALL each have an explicit byte ceiling."),
    ("PWB-REQ-006 scenario title", SPEC, "Resource breach is bounded and explicit"),
    ("PWB-REQ-006 scenario AND", SPEC, "human and machine responses stay within their own declared encoded-byte ceilings"),
    ("PWB-REQ-006 oracle", SPEC, "exact final encoded-byte counts"),
    (".18 briefing sentence", BRIEFING_PATCH, "the final encoded HTTP body for each authenticated derived read-only machine view response"),
    ("VIS-2 heading", VISION, "No evidence means Unknown, not success"),
)

COMPRESSION = re.compile(r"\bzlib\b|\bgzip|content-encoding|\bbrotli|createGzip|createDeflate", re.I)
HEX64 = re.compile(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")


def normalize(text: str) -> str:
    text = re.sub(r"(?m)^[ \t]*>[ \t]?", "", text)
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1-\2", text)
    return re.sub(r"\s+", " ", text)


def read(root: str, rel: str) -> str | None:
    path = os.path.join(root, rel)
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def check_quotes(root: str) -> list[str]:
    findings = []
    packet = read(root, PACKET)
    if packet is None:
        return [f"C1 packet missing: {PACKET}"]
    npacket = normalize(packet)
    for label, rel, text in QUOTES:
        body = read(root, rel)
        if body is None:
            findings.append(f"C1 {label}: source missing: {rel}")
            continue
        if normalize(text) not in normalize(body):
            findings.append(f"C1 {label}: not found in {rel}")
        if normalize(text) not in npacket:
            findings.append(f"C1 {label}: not quoted in the packet")
    return findings


def _apply_alone(root: str, patch_rel: str, target_rel: str) -> str | None:
    """Return the target's bytes after applying the patch alone, or None."""
    source = read(root, target_rel)
    if source is None:
        return None
    with tempfile.TemporaryDirectory() as tmp:
        dest = os.path.join(tmp, target_rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(source)
        proc = subprocess.run(
            ["git", "apply", "--whitespace=nowarn", os.path.join(root, patch_rel)],
            cwd=tmp, capture_output=True, text=True,
        )
        if proc.returncode != 0:
            return None
        with open(dest, encoding="utf-8") as fh:
            return fh.read()


def response_ceilings(text: str) -> set[str]:
    out = set()
    for key, value in re.findall(r'"(max[A-Za-z]*ResponseBytes)"\s*:\s*"([^"]*)"', text):
        if value.startswith(CEILING_PREFIX):
            out.add(key)
    return out


def check_ceilings(root: str) -> tuple[list[str], set[str]]:
    findings = []
    registry = read(root, REGISTRY)
    packet = read(root, PACKET) or ""
    if registry is None:
        return [f"C2 registry missing: {REGISTRY}"], set()
    keys = response_ceilings(registry)
    if read(root, BRIEFING_PATCH) is not None:
        patched = _apply_alone(root, BRIEFING_PATCH, REGISTRY)
        if patched is None:
            if "maxBriefingResponseBytes" not in registry:
                findings.append("C2 .18 patch neither applies nor has landed")
        else:
            keys |= response_ceilings(patched)
    for key in IN_FORCE_CEILINGS:
        if key not in keys:
            findings.append(f"C2 in-force ceiling {key} not found by the sentence predicate")
    for key in sorted(keys):
        if f"`{key}`" not in packet:
            findings.append(f"C2 response ceiling {key} is not named in the packet")
    return findings, keys


def check_no_compression(root: str) -> tuple[list[str], int, bool]:
    if os.path.isfile(os.path.join(root, DIRECTION)):
        return [], 0, True
    findings, scanned = [], 0
    for top in ("apps", "packages"):
        base = os.path.join(root, top)
        if not os.path.isdir(base):
            continue
        for pkg in sorted(os.listdir(base)):
            src = os.path.join(base, pkg, "src")
            for dirpath, dirnames, filenames in os.walk(src):
                dirnames[:] = sorted(d for d in dirnames if d not in ("node_modules", "dist", "test-fixtures"))
                for name in sorted(filenames):
                    if not re.search(r"\.m?ts$", name) or re.search(r"\.test\.m?ts$", name):
                        continue
                    scanned += 1
                    path = os.path.join(dirpath, name)
                    with open(path, encoding="utf-8") as fh:
                        for n, line in enumerate(fh, 1):
                            if COMPRESSION.search(line):
                                findings.append(f"C3 compression code before any direction: {os.path.relpath(path, root)}:{n}")
    if scanned == 0:
        findings.append("C3 compression sweep scanned zero source files")
    return findings, scanned, False


def check_packet_shape(root: str) -> tuple[list[str], int]:
    packet = read(root, PACKET)
    if packet is None:
        return [f"C4 packet missing: {PACKET}"], 0
    findings = []
    if "**Candidate — binds nothing.**" not in packet:
        findings.append("C4 candidate banner missing")
    section = re.search(r"(?ms)^## Open questions\n(.*?)(?=^## )", packet)
    if section is None:
        return findings + ["C4 no '## Open questions' section"], 0
    questions = re.split(r"(?m)^### ", section.group(1))[1:]
    if not questions:
        findings.append("C4 open-questions section holds no question")
    for q in questions:
        if "**Default if unanswered:**" not in q:
            findings.append(f"C4 question without a default: {q.splitlines()[0]}")
    if HEX64.search(packet):
        findings.append("C4 packet carries a 64-hex digest")
    return findings, len(questions)


def check_composition(root: str) -> tuple[list[str], int, list[str]]:
    by_path: dict[str, list[tuple[str, str]]] = {}
    for label, rel, text in QUOTES:
        by_path.setdefault(rel, []).append((label, text))
    findings, applied, skipped = [], 0, []
    base = os.path.join(root, CANDIDATES)
    patches = []
    if os.path.isdir(base):
        for pkg in sorted(os.listdir(base)):
            pdir = os.path.join(base, pkg, "proposed")
            if os.path.isdir(pdir):
                patches += [f"{CANDIDATES}/{pkg}/proposed/{n}" for n in sorted(os.listdir(pdir)) if n.endswith(".patch")]
    for patch_rel in patches:
        text = read(root, patch_rel) or ""
        for target in re.findall(r"(?m)^\+\+\+ b/(\S+)", text):
            if target not in by_path:
                continue
            after = _apply_alone(root, patch_rel, target)
            if after is None:
                skipped.append(f"{patch_rel} -> {target}")
                continue
            applied += 1
            for label, quote in by_path[target]:
                if normalize(quote) not in normalize(after):
                    findings.append(f"C5 {patch_rel} changes the quoted {label} in {target}")
    return findings, applied, skipped


def check(root: str = ROOT, verbose: bool = True) -> list[str]:
    findings = check_quotes(root)
    f2, keys = check_ceilings(root)
    f3, scanned, gated = check_no_compression(root)
    f4, nq = check_packet_shape(root)
    f5, applied, skipped = check_composition(root)
    findings += f2 + f3 + f4 + f5
    if verbose:
        print(f"C1 quoted clauses: {len(QUOTES)} checked in source and packet")
        print(f"C2 response ceilings named: {len(keys)} ({', '.join(sorted(keys))})")
        print("C3 compression sweep: gated off (direction exists)" if gated else f"C3 compression sweep: {scanned} non-test source files scanned")
        print(f"C4 open questions with a default: {nq}")
        print(f"C5 candidate patches touching quoted files applied alone: {applied}; not applicable alone: {len(skipped)}")
        for s in skipped:
            print(f"   not applicable alone: {s}")
        for f in findings:
            print(f"FAIL {f}")
        print("OK" if not findings else f"{len(findings)} finding(s)")
    return findings


# ---- selftest ------------------------------------------------------------

def _fixture_root(tmp: str) -> str:
    root = os.path.join(tmp, "root")
    rels = {PACKET, REGISTRY, RULINGS, CONTINUATION, RETENTION, ROUTES, SPEC, VISION}
    base = os.path.join(ROOT, CANDIDATES)
    for pkg in os.listdir(base):
        pdir = os.path.join(base, pkg, "proposed")
        if os.path.isdir(pdir):
            rels |= {f"{CANDIDATES}/{pkg}/proposed/{n}" for n in os.listdir(pdir) if n.endswith(".patch")}
    for rel in rels:
        dest = os.path.join(root, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(os.path.join(ROOT, rel), dest)
    return root


def _edit(root: str, rel: str, old: str, new: str) -> None:
    path = os.path.join(root, rel)
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if old not in text:
        raise AssertionError(f"selftest fixture: {old!r} not in {rel}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text.replace(old, new))


def _edit_ws(root: str, rel: str, phrase: str, new: str) -> None:
    """Replace every occurrence of phrase, however it is wrapped."""
    path = os.path.join(root, rel)
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    pattern = r"\s+(?:>\s*)?".join(re.escape(w) for w in phrase.split())
    text, n = re.subn(pattern, new, text)
    if n == 0:
        raise AssertionError(f"selftest fixture: {phrase!r} not in {rel}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _sibling_patch(root: str) -> None:
    rel = SPEC
    with open(os.path.join(root, rel), encoding="utf-8") as fh:
        lines = fh.read().splitlines(keepends=True)
    idx = next(i for i, line in enumerate(lines) if "explicit byte ceiling." in line)
    new = lines[:idx] + [lines[idx].replace("explicit byte ceiling.", "explicit byte allowance.")] + lines[idx + 1:]
    import difflib
    diff = "".join(difflib.unified_diff(lines, new, f"a/{rel}", f"b/{rel}"))
    dest = os.path.join(root, CANDIDATES, "zz-selftest", "proposed", "spec.md.patch")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(f"diff --git a/{rel} b/{rel}\n" + diff)


def selftest() -> int:
    cases = [
        ("baseline passes", None, None, True),
        ("C1 source quote drifts", "C1", lambda r: _edit(r, RULINGS, "The registry entry is edited on no arm.", "The registry entry is left alone."), False),
        ("C1 packet drops a quote", "C1", lambda r: _edit_ws(r, PACKET, "The registry entry is edited on no arm.", "The registry is left alone."), False),
        ("C2 registry gains an unnamed response ceiling", "C2", lambda r: _edit(r, REGISTRY, '"maxHumanResponseBytes": "the final', '"maxOtherResponseBytes": "the final encoded HTTP body for x",\n        "maxHumanResponseBytes": "the final'), False),
        ("C2 packet drops the briefing ceiling", "C2", lambda r: _edit(r, PACKET, "`maxBriefingResponseBytes`", "`the briefing ceiling`"), False),
        ("C3 compression code lands before a direction", "C3", lambda r: _edit(r, ROUTES, "const observed = Buffer", "const gz = require('node:zlib');\n  const observed = Buffer"), False),
        ("C3 an issued direction gates the sweep off", None, lambda r: (_edit(r, ROUTES, "const observed = Buffer", "const gz = require('node:zlib');\n  const observed = Buffer"), open(os.path.join(r, DIRECTION), "w").close()), True),
        ("C3 sweep over zero files", ("C3", "C1"), lambda r: shutil.rmtree(os.path.join(r, "apps")), False),
        ("C4 banner removed", "C4", lambda r: _edit(r, PACKET, "**Candidate — binds nothing.**", "**Draft.**"), False),
        ("C4 a question loses its default", "C4", lambda r: _edit(r, PACKET, "**Default if unanswered:** (a). No new dependency", "No new dependency"), False),
        ("C4 packet quotes a 64-hex digest", "C4", lambda r: _edit(r, PACKET, "## Impact\n", "## Impact\n\n" + "ab" * 32 + "\n"), False),
        ("C5 a sibling patch rewrites a quoted sentence", "C5", _sibling_patch, False),
    ]
    failed = 0
    for name, prefix, mutate, expect_ok in cases:
        with tempfile.TemporaryDirectory() as tmp:
            root = _fixture_root(tmp)
            if mutate is not None:
                mutate(root)
            findings = check(root, verbose=False)
            if expect_ok:
                ok = not findings
            else:
                allowed = prefix if isinstance(prefix, tuple) else (prefix,)
                ok = any(f.startswith(allowed[0]) for f in findings) and all(f.startswith(allowed) for f in findings)
            print(f"{'PASS' if ok else 'FAIL'} {name}" + ("" if ok else f": {findings}"))
            failed += not ok
    print(f"selftest: {len(cases) - failed}/{len(cases)} passed")
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    return 1 if check() else 0


if __name__ == "__main__":
    sys.exit(main())
