#!/usr/bin/env python3
"""Static site equivalence for syzygy-bpyt.6.3: every hash and freeze call keeps its argument text.

Usage: site-equivalence.py <repo> <base-commit> <head-commit> [--selftest]

For each production source file (the sweep.py population) that differs between the two commits, compare the
multiset of arguments passed to the hash and freeze helpers:

  hash    at <base>  `createHash('sha256').update(ARG[, 'utf8']).digest('hex')`, and `sha256(ARG)` / `digest(ARG)`
                     calls to a file-local helper;
          at <head>  `sha256(ARG)` calls.
  freeze  `deepFreeze(ARG)` calls at both.

ARG is compared as written, with whitespace runs collapsed. A definition (`function sha256(`, `const sha256 =`)
is not a call. The base-side local helpers are also checked to be the canonical one-argument form, so a call's
argument reaches `.update(...)` unchanged. A file whose multisets differ is listed with both sides; helpers that
were exported and moved callers (`act-fields.ts` exported `sha256`) show as a difference per file and are
reconciled by the global multiset, which must be equal.
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sweep  # noqa: E402  (same directory)

HASH_BASE_INLINE = re.compile(r"""createHash\(\s*['"]sha256['"]\s*\)\s*\.update\(""")
CALL = re.compile(r'(?<![.\w$])(sha256|digest|deepFreeze)\(')
DEF_BEFORE = re.compile(r'(?:function\s+|export\s+function\s+)$')
CANONICAL_DEF = [
    re.compile(r"^(?:export )?const (?P<n>sha256|digest) = \((?P<p>\w+): (?:string|string \| Uint8Array)\)(?:: string)? =>\s*createHash\('sha256'\)\.update\((?P=p)\)\.digest\('hex'\);$", re.M),
    re.compile(r"^(?:export )?function (?P<n>sha256)\((?P<p>\w+): (?:string|string \| Uint8Array)\): string \{\n  return createHash\('sha256'\)\.update\((?P=p)\)\.digest\('hex'\);\n\}$", re.M),
]


def blob(repo, commit, path):
    run = subprocess.run(['git', '-C', repo, 'cat-file', '-p', f'{commit}:{path}'], capture_output=True)
    return run.stdout.decode('utf-8') if run.returncode == 0 else None


def norm(arg):
    return re.sub(r'\s+', ' ', arg).strip()


def call_args(text, names):
    """Arguments of each call to one of `names` (not a definition), as (name, normalised argument)."""
    found = []
    for m in CALL.finditer(text):
        if m.group(1) not in names:
            continue
        if DEF_BEFORE.search(text[max(0, m.start() - 20):m.start()]):
            continue
        open_at = m.end() - 1
        close = sweep.skip_balanced(text, open_at, '(', ')')
        found.append((m.group(1), norm(text[open_at + 1:close - 1])))
    return found


def inline_hash_args(text):
    found = []
    for m in HASH_BASE_INLINE.finditer(text):
        open_at = m.end() - 1
        close = sweep.skip_balanced(text, open_at, '(', ')')
        if not text.startswith(".digest('hex')", close):
            continue
        args = sweep.top_level_arguments(text[open_at + 1:close - 1])
        if len(args) == 1 or (len(args) == 2 and args[1] == "'utf8'"):
            found.append(('sha256', norm(args[0])))
    return found


def base_hash_sites(text):
    """Inline sites plus calls to a local helper; the helper's own body is not counted (it is a definition)."""
    inline = inline_hash_args(text)
    # the body of a local definition is an inline site too: drop those, they are the helper, not a use
    defs = [m for rx in CANONICAL_DEF for m in rx.finditer(text)]
    for m in defs:
        inline.remove(('sha256', m.group('p')))
    return inline + call_args(text, {'sha256', 'digest'}), [m.group(0) for m in defs]


def head_hash_sites(text):
    return inline_hash_args(text) + call_args(text, {'sha256'})


def tally(items):
    out = {}
    for item in items:
        out[item] = out.get(item, 0) + 1
    return out


def population_changes(repo, base, head):
    names = subprocess.run(['git', '-C', repo, 'diff', '--name-only', '-z', base, head], capture_output=True, check=True).stdout.decode().split('\0')
    return sorted(n for n in names if n and sweep.POPULATION.match(n) and not sweep.TEST_FILE.search(n))


def freeze_defs(text):
    return [m.start() for m in re.finditer(r'(?:export )?function deepFreeze<T>\(value: T\): T \{', text)]


def normalised_freeze_body(text):
    m = re.search(r'(?:export )?function deepFreeze<T>\(value: T\): T \{\n((?:.*\n)*?)\}\n', text)
    return None if m is None else norm(m.group(1))


def compare(repo, base, head):
    files = population_changes(repo, base, head)
    rows, global_base, global_head = [], {}, {}
    freeze_base, freeze_head = {}, {}
    noncanonical, freeze_bodies = [], {}
    for path in files:
        before, after = blob(repo, base, path), blob(repo, head, path)
        if before is None or after is None:
            rows.append({'file': path, 'note': 'added' if before is None else 'deleted'})
            continue
        base_sites, defs = base_hash_sites(before)
        head_sites = head_hash_sites(after)
        for d in defs:
            if not any(rx.match(d) for rx in CANONICAL_DEF):
                noncanonical.append({'file': path, 'def': d})
        base_freeze, head_freeze = call_args(before, {'deepFreeze'}), call_args(after, {'deepFreeze'})
        if freeze_defs(before):
            freeze_bodies[path] = normalised_freeze_body(before)
        for k, v in tally(base_sites).items():
            global_base[k] = global_base.get(k, 0) + v
        for k, v in tally(head_sites).items():
            global_head[k] = global_head.get(k, 0) + v
        for k, v in tally(base_freeze).items():
            freeze_base[k] = freeze_base.get(k, 0) + v
        for k, v in tally(head_freeze).items():
            freeze_head[k] = freeze_head.get(k, 0) + v
        # head-side `sha256` and `digest` are one name: compare on the argument
        hb = tally([a for _, a in base_sites])
        hh = tally([a for _, a in head_sites])
        fb = tally([a for _, a in base_freeze])
        fh = tally([a for _, a in head_freeze])
        rows.append({'file': path, 'hashSites': {'base': sum(hb.values()), 'head': sum(hh.values()), 'equal': hb == hh},
                     'freezeCalls': {'base': sum(fb.values()), 'head': sum(fh.values()), 'equal': fb == fh},
                     **({} if hb == hh and fb == fh else {'baseOnly': {k: v - hh.get(k, 0) for k, v in hb.items() if v != hh.get(k, 0)},
                                                          'headOnly': {k: v - hb.get(k, 0) for k, v in hh.items() if v != hb.get(k, 0)}})})
    gb, gh = {}, {}
    for (name, arg), n in global_base.items():
        gb[arg] = gb.get(arg, 0) + n
    for (name, arg), n in global_head.items():
        gh[arg] = gh.get(arg, 0) + n
    fb_, fh_ = {}, {}
    for (name, arg), n in freeze_base.items():
        fb_[arg] = fb_.get(arg, 0) + n
    for (name, arg), n in freeze_head.items():
        fh_[arg] = fh_.get(arg, 0) + n
    return {
        'base': base, 'head': head,
        'files': len(files),
        'filesCompared': sum(1 for r in rows if 'hashSites' in r),
        'filesWhoseHashArgumentsDiffer': [r['file'] for r in rows if 'hashSites' in r and not r['hashSites']['equal']],
        'filesWhoseFreezeArgumentsDiffer': [r['file'] for r in rows if 'freezeCalls' in r and not r['freezeCalls']['equal']],
        'globalHashArguments': {'base': sum(gb.values()), 'head': sum(gh.values()), 'equal': gb == gh},
        'globalFreezeArguments': {'base': sum(fb_.values()), 'head': sum(fh_.values()), 'equal': fb_ == fh_},
        'noncanonicalLocalHelpers': noncanonical,
        'baseFreezeBodies': freeze_bodies,
        'rows': rows,
    }


def selftest():
    cases = []

    def check(label, ok):
        cases.append((label, ok))
    inline = "const a = createHash('sha256').update(x + 'y', 'utf8').digest('hex');"
    check('inline utf8 argument', inline_hash_args(inline) == [('sha256', "x + 'y'")])
    check('digest(\'base64\') is not a hex site', inline_hash_args("createHash('sha256').update(x).digest('base64')") == [])
    check('definition is not a call', call_args('function sha256(value: string): string {', {'sha256'}) == [])
    check('call with nested parens', call_args('const a = sha256(f(g(1), "h)"));', {'sha256'}) == [('sha256', 'f(g(1), "h)")')])
    check('method .digest( is not the alias', call_args('h.update(x).digest("hex")', {'digest'}) == [])
    defn = "const sha256 = (value: string): string => createHash('sha256').update(value).digest('hex');\nconst k = sha256(a);\n"
    sites, defs = base_hash_sites(defn)
    check('local arrow definition dropped, call kept', sites == [('sha256', 'a')] and len(defs) == 1)
    fdef = "function sha256(value: string): string {\n  return createHash('sha256').update(value).digest('hex');\n}\nfoo(sha256(b));\n"
    sites, defs = base_hash_sites(fdef)
    check('local function definition dropped, call kept', sites == [('sha256', 'b')] and len(defs) == 1)
    check('canonical regex rejects a transforming helper', not any(rx.match("const sha256 = (value: string): string => createHash('sha256').update(value.trim()).digest('hex');") for rx in CANONICAL_DEF))
    check('tally', tally([1, 1, 2]) == {1: 2, 2: 1})
    return {'cases': len(cases), 'failures': [label for label, ok in cases if not ok]}


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        result = selftest()
        print(json.dumps(result))
        sys.exit(1 if result['failures'] else 0)
    print(json.dumps(compare(sys.argv[1], sys.argv[2], sys.argv[3]), indent=1))
