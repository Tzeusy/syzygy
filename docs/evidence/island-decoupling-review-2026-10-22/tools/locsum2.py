"""One line per shifted locator in the lane's locators.json, plus a census of citer classes and reasons. Usage: locsum2.py <locators.json>"""
import collections, json, sys
d = json.load(open(sys.argv[1]))
t = d['shiftedTable']
print('shiftedTable rows', len(t), 'shiftedRows', len(d['shiftedRows']))
for r in t:
    print(r['citer'], r['citerLine'], r['locator'], r['citerClass'], 'reviewed', r.get('reviewedCommit'), 'eqOld', r.get('citedLinesAtReviewedCommitEqualOld'), '|', r['whyNoRepair'][:60])
print(collections.Counter(r['citerClass'] for r in t))
print(collections.Counter(r['whyNoRepair'] for r in t))
nonraw = [r for r in d['shiftedRows'] if r['citerBound'] != 'review raw']
print('shifted rows whose citer is not a review raw:', len(nonraw))
for r in nonraw: print('  ', json.dumps(r))
print('rows with citer in governed plane:', sum(1 for r in d['rows'] if r['citer'].startswith(('.syzygy/', 'openspec/'))))
gov_shift = [r for r in d['rows'] if r['citer'].startswith(('.syzygy/', 'openspec/')) and r['accurateAtOld'] and not r['citedLinesUnchanged']]
print('governed-plane rows accurate at old and shifted:', len(gov_shift))
