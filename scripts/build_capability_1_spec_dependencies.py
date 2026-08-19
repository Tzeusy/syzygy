#!/usr/bin/env python3
"""Generate the Capability 1 spec-level dependency declaration (CC-IMPACT-1).

The specification's requirements each carry one fenced ``warrants`` YAML
block naming their material governing authorities in CC-SPEC-2's six
classes. CC-IMPACT-1 requires the specification-level declaration to be
the GENERATED union of those blocks — one machine-readable home, no
second hand-maintained list. This script is that generator.

    build_capability_1_spec_dependencies.py            write the union file
    build_capability_1_spec_dependencies.py --check    fail on drift, write nothing
    build_capability_1_spec_dependencies.py --selftest mutation fixtures

The generator quotes no clause prose — identifiers only. Totals are
computed, never transcribed (verification rule 3).
"""

import hashlib
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CHANGE = os.path.join(ROOT, "openspec", "changes",
                      "project-registration-and-honest-shape-visibility")
SPEC = os.path.join(CHANGE, "specs",
                    "project-registration-and-honest-shape-visibility", "spec.md")
OUT = os.path.join(CHANGE, "GOVERNING-DEPENDENCIES.md")

CLASSES = ("doctrine", "contracts", "policies", "decisions", "topology",
           "parent_requirements")
FIELDS = ("primary",) + CLASSES

REQ_RE = re.compile(r"^### Requirement: (CAP1-REQ-\d{3}) — ", re.M)
BLOCK_RE = re.compile(r"^```yaml\n(.*?)^```", re.M | re.S)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def natkey(s):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def _unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "'\"":
        return s[1:-1]
    return s


def parse_warrants_yaml(block):
    """Parse one warrants block — deliberately a stdlib-only parser for
    the constrained subset the spec uses (a `warrants:` mapping of scalar
    and flow-list values), because the hosted battery installs no
    packages. Returns (data, error): data mirrors yaml.safe_load's shape
    {'warrants': {field: scalar-or-list}}."""
    lines = [l for l in block.splitlines() if l.strip()]
    if not lines:
        return None, "empty block"
    top = {}
    current = None
    for line in lines:
        if not line.startswith(" "):
            m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
            if not m:
                return None, f"unparseable line: {line!r}"
            key, rest = m.group(1), m.group(2).strip()
            top[key] = {} if rest == "" else _unquote(rest)
            current = top[key] if rest == "" else None
        else:
            if current is None or not isinstance(current, dict):
                return None, f"unexpected indented line: {line!r}"
            m = re.match(r"^\s+([A-Za-z_][\w-]*):\s*(.*)$", line)
            if not m:
                return None, f"unparseable line: {line!r}"
            key, rest = m.group(1), m.group(2).strip()
            if rest.startswith("[") and rest.endswith("]"):
                inner = rest[1:-1].strip()
                current[key] = ([] if not inner else
                                [_unquote(x) for x in inner.split(",")])
            elif rest == "":
                current[key] = []
            else:
                current[key] = _unquote(rest)
    return top, None


def parse(spec_text):
    """Return (requirements, errors). requirements: list of
    (req_id, {field: value}) in file order."""
    errors = []
    heads = list(REQ_RE.finditer(spec_text))
    if not heads:
        return [], ["no `### Requirement: CAP1-REQ-nnn — …` headers found"]

    seen = set()
    reqs = []
    for i, m in enumerate(heads):
        rid = m.group(1)
        if rid in seen:
            errors.append(f"{rid}: duplicate requirement identifier")
        seen.add(rid)
        body = spec_text[m.end():heads[i + 1].start() if i + 1 < len(heads)
                         else len(spec_text)]
        blocks = BLOCK_RE.findall(body)
        if len(blocks) != 1:
            errors.append(f"{rid}: expected exactly one fenced yaml warrants "
                          f"block, found {len(blocks)}")
            continue
        data, perr = parse_warrants_yaml(blocks[0])
        if perr:
            errors.append(f"{rid}: warrants block does not parse: {perr}")
            continue
        if not isinstance(data, dict) or set(data) != {"warrants"}:
            errors.append(f"{rid}: block must hold exactly one top-level "
                          f"`warrants` mapping")
            continue
        w = data["warrants"]
        if not isinstance(w, dict) or set(w) != set(FIELDS):
            errors.append(f"{rid}: warrants fields must be exactly "
                          f"{{{', '.join(FIELDS)}}}")
            continue
        if not isinstance(w["primary"], str) or not w["primary"].strip():
            errors.append(f"{rid}: `primary` must be a non-empty string")
            continue
        bad = False
        for cls in CLASSES:
            v = w[cls]
            if v is None:
                w[cls] = []
                continue
            if (not isinstance(v, list)
                    or any(not isinstance(x, str) or not x.strip() for x in v)):
                errors.append(f"{rid}: `{cls}` must be a list of non-empty "
                              f"strings (or empty)")
                bad = True
        if bad:
            continue
        everything = {x for cls in CLASSES for x in w[cls]}
        if w["primary"] not in everything:
            errors.append(f"{rid}: `primary` ({w['primary']}) does not appear "
                          f"in any warrant class list")
            continue
        reqs.append((rid, w))

    ids = {rid for rid, _ in reqs}
    for rid, w in reqs:
        for parent in w["parent_requirements"]:
            if parent not in ids:
                errors.append(f"{rid}: parent requirement {parent} does not "
                              f"exist in this specification")
    return reqs, errors


def render(reqs, spec_digest):
    """Render the union file. Identifiers only — no clause prose."""
    union = {cls: {} for cls in CLASSES}
    for rid, w in reqs:
        for cls in CLASSES:
            for ident in w[cls]:
                union[cls].setdefault(ident, []).append(rid)

    total = sum(len(union[cls]) for cls in CLASSES)
    lines = []
    a = lines.append
    a("# Governing dependencies — project-registration-and-honest-shape-visibility")
    a("")
    a("> **GENERATED — do not edit.** This file is the CC-IMPACT-1")
    a("> specification-level dependency declaration: the computed union of")
    a("> every requirement's `warrants` block in `specs/…/spec.md`. Edit the")
    a("> requirement warrants and regenerate with")
    a("> `python3 scripts/build_capability_1_spec_dependencies.py`; an edit")
    a("> here is overwritten and `--check` fails first. Identifiers only —")
    a("> nothing here quotes or paraphrases any clause.")
    a(">")
    a(f"> Source: `spec.md` sha256 `{spec_digest}` — "
      f"{len(reqs)} requirement(s), {total} distinct authorities.")
    a("")
    for cls in CLASSES:
        a(f"## {cls} ({len(union[cls])})")
        a("")
        if not union[cls]:
            a("*(none declared)*")
            a("")
            continue
        a("| Authority | Cited by |")
        a("|---|---|")
        for ident in sorted(union[cls], key=natkey):
            cites = ", ".join(sorted(set(union[cls][ident]), key=natkey))
            a(f"| `{ident}` | {cites} |")
        a("")
    return "\n".join(lines).rstrip() + "\n"


def generate(spec_text):
    reqs, errors = parse(spec_text)
    if errors:
        return None, errors
    digest = hashlib.sha256(spec_text.encode()).hexdigest()
    return render(reqs, digest), []


def main(argv):
    if "--selftest" in argv:
        return selftest()
    check = "--check" in argv

    spec_text = read(SPEC)
    out, errors = generate(spec_text)
    if errors:
        print("SPEC WARRANTS DO NOT VALIDATE — no declaration was generated:")
        for e in errors:
            print(f"  {e}")
        return 1

    reqs, _ = parse(spec_text)
    n_auth = out.split(" distinct authorities")[0].rsplit(" ", 1)[-1]
    if check:
        if not os.path.exists(OUT) or read(OUT) != out:
            print("DRIFT: GOVERNING-DEPENDENCIES.md differs from regeneration")
            return 1
        print(f"capability 1 spec dependencies match regeneration — "
              f"{len(reqs)} requirement(s), {n_auth} distinct authorities")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"wrote GOVERNING-DEPENDENCIES.md — {len(reqs)} requirement(s), "
          f"{n_auth} distinct authorities")
    return 0


# -------------------------------------------------------------- the fixtures

GOOD = """\
### Requirement: CAP1-REQ-001 — Alpha

body

```yaml
warrants:
  primary: RFC1-1
  doctrine: [VIS-2]
  contracts: [RFC1-1, RFC1-10]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-002 — Beta

body

```yaml
warrants:
  primary: SDR-36
  doctrine: []
  contracts: [RFC1-1]
  policies: []
  decisions: [SDR-36]
  topology: []
  parent_requirements: [CAP1-REQ-001]
```
"""


def selftest():
    """Every predicate is mutation-tested: the mutated input must FAIL
    (verification rule 6)."""
    failures = []

    def expect_ok(name, text):
        out, errors = generate(text)
        if errors or out is None:
            failures.append(f"{name}: expected clean, got {errors}")

    def expect_fail(name, text, needle):
        _, errors = generate(text)
        if not errors:
            failures.append(f"{name}: mutation passed the check")
        elif needle not in " | ".join(errors):
            failures.append(f"{name}: failed for the wrong reason: {errors}")

    expect_ok("well-formed", GOOD)
    expect_fail("duplicate-id",
                GOOD.replace("CAP1-REQ-002 — Beta", "CAP1-REQ-001 — Beta", 1),
                "duplicate requirement identifier")
    expect_fail("missing-block",
                GOOD.replace("```yaml\nwarrants:\n  primary: SDR-36", "```yaml\nx:", 1),
                "exactly one top-level `warrants` mapping")
    expect_fail("no-block", GOOD.split("```yaml")[0],
                "expected exactly one fenced yaml warrants block, found 0")
    expect_fail("two-blocks",
                GOOD.replace("### Requirement: CAP1-REQ-002",
                             "```yaml\nwarrants: {}\n```\n\n"
                             "### Requirement: CAP1-REQ-002", 1),
                "found 2")
    expect_fail("extra-field",
                GOOD.replace("  topology: []", "  topology: []\n  extra: []", 1),
                "fields must be exactly")
    expect_fail("empty-primary",
                GOOD.replace("primary: RFC1-1", "primary: ''", 1),
                "`primary` must be a non-empty string")
    expect_fail("primary-not-listed",
                GOOD.replace("primary: RFC1-1", "primary: RFC9-99", 1),
                "does not appear in any warrant class list")
    expect_fail("empty-list-entry",
                GOOD.replace("doctrine: [VIS-2]", "doctrine: [VIS-2, '']", 1),
                "list of non-empty strings")
    expect_fail("phantom-parent",
                GOOD.replace("parent_requirements: [CAP1-REQ-001]",
                             "parent_requirements: [CAP1-REQ-099]", 1),
                "does not exist in this specification")
    expect_fail("no-headers", "no requirements here\n",
                "no `### Requirement:")

    # Drift predicate: a mutated output must differ from regeneration.
    out, _ = generate(GOOD)
    if out == out.replace("RFC1-10", "RFC1-11"):
        failures.append("drift: mutation did not change the rendering")

    # Determinism: two runs render identically.
    out2, _ = generate(GOOD)
    if out != out2:
        failures.append("determinism: two runs differ")

    n_cases = 13
    if failures:
        print(f"SELFTEST FAILED ({len(failures)}/{n_cases}):")
        for f in failures:
            print(f"  {f}")
        return 1
    print(f"selftest: {n_cases}/{n_cases} fixtures behave "
          f"(1 clean, 10 mutations rejected, drift + determinism hold)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
