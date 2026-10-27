"""Line conservation (rev-510): every line of an old file, after the stated renames and with an `export ` prefix ignored, must appear
in the union of the new files; lines only in the new files are listed (hand-written headers, imports, re-exports).
Usage: conserve.py <repo> <old commit> <old path> <new commit> <new path>... [--rename A=B ...]"""
import collections, re, subprocess, sys
args = sys.argv[1:]
renames = []
if '--rename' in args:
    i = args.index('--rename'); renames = [tuple(r.split('=')) for r in args[i + 1:]]; args = args[:i]
repo, old_commit, old_path, new_commit, *new_paths = args
show = lambda c, p: subprocess.run(['git', '-C', repo, 'show', f'{c}:{p}'], capture_output=True, check=True).stdout.decode()
def norm(line):
    for a, b in renames: line = re.sub(rf'\b{a}\b', b, line)
    line = line.rstrip()
    return line[len('export '):] if line.startswith('export ') else line
old = collections.Counter(norm(l) for l in show(old_commit, old_path).split('\n') if l.strip())
new = collections.Counter()
for p in new_paths: new.update(norm(l) for l in show(new_commit, p).split('\n') if l.strip())
missing = old - new
added = new - old
print(f'old non-blank lines {sum(old.values())}; new non-blank lines {sum(new.values())}; old lines not in new: {sum(missing.values())}; new lines not in old: {sum(added.values())}')
for l, n in missing.items(): print('  MISSING', n, l[:220])
for l, n in added.items(): print('  ADDED  ', n, l[:220])
