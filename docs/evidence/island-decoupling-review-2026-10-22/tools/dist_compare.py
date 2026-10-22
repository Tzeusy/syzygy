"""Compare compiled .js files of a package directory between two trees. Usage: dist_compare.py <old root> <new root> <rel dist dir>..."""
import hashlib, pathlib, sys
old, new, *dirs = sys.argv[1:]
for d in dirs:
    a = {p.relative_to(pathlib.Path(old) / d).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in (pathlib.Path(old) / d).rglob('*.js')}
    b = {p.relative_to(pathlib.Path(new) / d).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in (pathlib.Path(new) / d).rglob('*.js')}
    same = sorted(k for k in a if b.get(k) == a[k])
    differ = sorted(k for k in a if k in b and b[k] != a[k])
    print(f'{d}: old {len(a)} new {len(b)} identical {len(same)} differ {differ} only-old {sorted(set(a) - set(b))} only-new {sorted(set(b) - set(a))}')
