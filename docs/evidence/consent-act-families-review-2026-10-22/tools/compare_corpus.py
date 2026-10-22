"""Compare the PROSE_ALTERATIONS / HEAD_FIELD_ALTERATION copy in the differential script with PR #500's testkit at c08a015d."""
import re
import sys

testkit = open(sys.argv[1], encoding='utf-8').read()
script = open(sys.argv[2], encoding='utf-8').read()


def block(text, start, end):
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]


a = block(testkit, 'export const PROSE_ALTERATIONS', '/** The control')
a += block(testkit, 'export const HEAD_FIELD_ALTERATION', '\n\n')
b = block(script, 'const PROSE_ALTERATIONS', '\n\nconst TYPE_LINE')


def norm(t):
    t = t.replace('export const', 'const')
    t = re.sub(r': ReadonlyArray<readonly \[name: string, alter: \(text: string\) => string\]> = Object\.freeze\(\[', ' = [', t)
    t = t.replace(']);\n', '];\n')
    t = t.replace('(text: string) =>', 'text =>')
    t = t.replace('(text: string): string =>', 'text =>')
    t = t.replace(' as const) {', ') {')
    t = re.sub(r'/\*\*[^\n]*\*/\n', '', t)
    return t.strip()


na, nb = norm(a), norm(b)
print('testkit block sha-free length', len(na), 'script block length', len(nb))
print('EQUAL after stripping TS annotations' if na == nb else 'DIFFERENT')
if na != nb:
    import difflib
    for line in difflib.unified_diff(na.splitlines(), nb.splitlines(), 'testkit', 'script', lineterm=''):
        print(line)
# Every regex literal and string literal of the testkit block appears in the script block.
lits = re.findall(r"/(?:[^/\n\\]|\\.)+/[gmsuy]*|'(?:[^'\\\n]|\\.)*'", a)
missing = [x for x in lits if x not in b]
print('literals in testkit block:', len(lits), 'missing from script:', len(missing))
for x in missing:
    print('  missing:', x)
