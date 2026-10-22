"""Replace exactly one occurrence of argv[2] by argv[3] in file argv[1]; fail unless the old text occurs exactly once."""
import sys

path, old, new = sys.argv[1], sys.argv[2], sys.argv[3]
text = open(path, encoding='utf-8').read()
count = text.count(old)
if count != 1:
    sys.exit(f'{old!r} occurs {count} times in {path}')
open(path, 'w', encoding='utf-8').write(text.replace(old, new, 1))
print('replaced 1 occurrence in', path)
