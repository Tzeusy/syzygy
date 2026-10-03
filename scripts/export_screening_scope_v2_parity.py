#!/usr/bin/env python3
"""Print the screening-scope v2 parity set for the TypeScript reader.

The TS port of the `project-documentation` path rule
(`apps/three-surface-poc/src/polaris-generation/project-documentation.ts`)
must give the builder's reference reading
(`scripts/build_public_source_screening_scope_v2.py`, `classify_documentation`)
for every path. This script imports that builder and prints, as JSON:

- per variant (`variantOrder`), the rule object exactly as the policy carries
  it, and the prerequisite object;
- the builder's own fixtures (`FIXTURES`, `OPT_IN_FIXTURES`) as `[path,
  [verdict per variant]]`;
- a generated path set (directory prefixes x names, plus seeded random paths
  over an alphabet that includes separators, digits, case and non-ASCII look-
  alikes) in the same row form, each verdict the reference reader's.

The committed snapshot `.../fixtures/screening-scope-v2-parity.json` is this
output. The parity test compares the TS reader with the snapshot, and, when the
builder is present, the snapshot with a fresh run of this script. Reads no
repository body and calls nothing over a network.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import pathlib
import random
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BUILDER = pathlib.Path("scripts/build_public_source_screening_scope_v2.py")

PREFIXES = ["", "docs/", "doc/", "Docs/", "DOCS/", "docs/a/", "docs/a/b/", "doc/guide/", "docs/adr/",
            "docs/My Design/", "docs/x.spec/", "docs/ſpec/", "docs/Architecture/", "docs/manifestos/",
            "docs/policyholder/", "docs/../", "docs//", "licenses/", "LICENSES/", "licenses/sub/",
            "license/", "src/", ".github/", "deps/lua/", "api-docs/", "design/", "./", "/"]
NAMES = ["README", "readme.md", "ReadMe.Md", "README.rst", "README.txt", "README.html", "README.md.bak",
         "README.md ", "00-README.md", "0-README.md", "123-README.md", "12-LICENSE", "1a-NEWS", "99_FAQ.md",
         "٠١-README.md", "CHANGELOG", "CHANGES.txt", "RELEASE-NOTES.rst", "RELEASE_NOTES", "RELEASENOTES",
         "CONTRIBUTING.md", "LICENSE", "LICENCE.md", "LICENſE", "COPYING", "NOTICE", "NOTICES.txt", "NEWS",
         "HISTORY.md", "AUTHORS", "FAQ.md", "ARCHITECTURE.md", "Manifesto", "00-MANIFESTO.txt", "SECURITY.md",
         "DESIGN.md", "GOVERNANCE", "CODE_OF_CONDUCT.md", "Code-Of-Conduct.md", "guide.md", "intro.rst",
         "usage.txt", "notes.TXT", ".md", "x.md.md", "spec.md", "x-spec.md", "x_spec.md", "x.spec.md",
         "x spec.md", "specimen.md", "SecurityPolicy.md", "spec(v2).md", "designer.md", "the-design-of-x.md",
         "architectures.md", "manifesto-why.md", "CMakeLists.txt", "CMAKELISTS.txt", "CMAKEKLISTS.txt",
         "robots.txt", "requirements.txt", "requirements-dev.txt", "Requirements.md", "agpl-3.0.txt",
         "rsal.TXT", "x.py", "conf.py", "diagram.png", "READMEİ.md", "README\\x.md", ""]
ALPHABET = list("aAzZ09-_. /\\") + ["d", "o", "c", "s", "r", "e", "a", "m", "l", "i", "n", "t", "x", "p",
                                     ".md", ".rst", ".txt", "docs", "licenses", "readme", "spec", "ſ",
                                     "K", "İ", "١", "\U0001F600"]


def reference_set(build) -> dict:
    variants = list(build.VARIANTS)
    rules = {v: build.documentation_rule(v) for v in variants}
    fixtures = [[p, [e for _v in variants]] for p, e in build.FIXTURES]
    fixtures += [[p, [k in build.VARIANTS[v] for v in variants]] for p, k in build.OPT_IN_FIXTURES]
    rng = random.Random(20261004)
    generated = [a + b for a, b in itertools.product(PREFIXES, NAMES)]
    generated += ["".join(rng.choice(ALPHABET) for _ in range(rng.randint(1, 8))) for _ in range(3000)]
    seen: set[str] = {f[0] for f in fixtures}
    paths = [p for p in generated if not (p in seen or seen.add(p))]
    return {
        "builder": BUILDER.as_posix(),
        "builderSha256": hashlib.sha256((ROOT / BUILDER).read_bytes()).hexdigest(),
        "variantOrder": variants,
        "rules": rules,
        "prerequisite": build.PREREQUISITE,
        "fixtures": fixtures,
        "generated": [[p, [build.classify_documentation(p, rules[v]) for v in variants]] for p in paths],
    }


def main() -> int:
    if not (ROOT / BUILDER).is_file():
        print(f"no builder at {BUILDER.as_posix()}", file=sys.stderr)
        return 2
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_public_source_screening_scope_v2 as build  # noqa: E402
    for p, e in build.FIXTURES:
        if build.classify_documentation(p) != e:
            print(f"builder fixture disagrees with its own reader: {p!r}", file=sys.stderr)
            return 1
    doc = reference_set(build)
    lists = {k: doc.pop(k) for k in ("fixtures", "generated")}
    head = json.dumps(doc, indent=1, ensure_ascii=True)[:-2]
    body = ",\n".join(f' "{k}": [\n' + ",\n".join("  " + json.dumps(row, ensure_ascii=True) for row in rows) + "\n ]"
                      for k, rows in lists.items())
    sys.stdout.write(head + ",\n" + body + "\n}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
