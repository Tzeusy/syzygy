import { describe, expect, it } from 'vitest';

import { generationSourcesForBody, gitBlobObjectId, type GenerationSource } from './generation-source.js';
import { QUOTE_LEAD_IN, checkBlockQuotes, inspectBlockQuotes, normaliseForQuote, quoteFindingAsReviewFinding, sourceTextById } from './quote-fidelity.js';

const files = (rows: readonly (readonly [string, string])[]) => rows.flatMap(([sourceId, body]) => generationSourcesForBody({ sourceId, repositoryId: 'repository:fixture', revision: 'a'.repeat(40), path: `${sourceId}.txt`, objectId: gitBlobObjectId(body), evaluationId: 'evaluation:fixture', body }));

const SOURCES = sourceTextById(files([
  ['src-readme', 'Tidemark is an in-memory cache.\nWe chose a **single-threaded** event loop because it avoids\n  lock   contention. See [the design notes](docs/design.md) for _why_.\n'],
  ['src-code', '/**\n * maybeEvict samples 5 keys\n * and evicts the least recently used key.\n */\n// Never block the loop.\n# Setting: maxmemory\nint x = 1;\n'],
  ['src-nested', 'The docs say "never block" and then "stop" loudly; he said “quiet “inner” words” too.'],
]));
const block = (text: string, ...sourceIds: string[]) => ({ id: 'b1', text, sourceIds });
const kinds = (text: string, ...sourceIds: string[]): string[] => checkBlockQuotes(block(text, ...sourceIds), SOURCES).map(f => f.kind);

describe('normaliseForQuote', () => {
  it('drops comment leaders, link syntax and emphasis, and collapses every whitespace run', () => {
    expect(normaliseForQuote('/**\n * maybeEvict samples 5 keys\n * and evicts.\n */\n// Never block.\n# Setting')).toBe('maybeEvict samples 5 keys and evicts. Never block. Setting');
    expect(normaliseForQuote('See [the design notes](docs/design.md) and ![a diagram](x.png) and [ref][1]')).toBe('See the design notes and a diagram and ref');
    expect(normaliseForQuote('a **bold** and _em_ and *x*')).toBe('a bold and em and x');
    expect(normaliseForQuote('  one \t two\r\nthree\n\n four  ')).toBe('one two three four');
  });
});

describe('checkBlockQuotes', () => {
  it('passes a quote that is a substring of a cited source, whatever the whitespace, emphasis or link syntax', () => {
    expect(kinds('The project states: "We chose a single-threaded event loop because it avoids lock contention."', 'src-readme')).toEqual([]);
    expect(kinds('It says "See the design notes for why."', 'src-readme')).toEqual([]);
    expect(kinds('The code says "maybeEvict samples 5 keys and evicts the least recently used key." and "Never block the loop."', 'src-code')).toEqual([]);
    expect(kinds('A comment: "Setting: maxmemory".', 'src-code')).toEqual([]);
    expect(kinds('He said “Tidemark is an in-memory cache.”', 'src-readme')).toEqual([]);
  });

  it('fails a quote that is not in any cited source, or only in an uncited one', () => {
    expect(kinds('"Tidemark is a distributed cache."', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
    expect(kinds('"Tidemark IS an in-memory cache."', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
    expect(kinds('"maybeEvict samples 5 keys"', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
    expect(kinds('"maybeEvict samples 5 keys"', 'src-readme', 'src-code')).toEqual([]);
    // Two cited sources do not join: a quote spanning the end of one and the start of the next is in neither.
    expect(kinds('"for why. maybeEvict samples 5 keys"', 'src-readme', 'src-code')).toEqual(['quote-not-in-cited-sources']);
  });

  it('checks every quoted span in a block, not just the first', () => {
    expect(kinds('"Tidemark is an in-memory cache." but also "invented words".', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
    expect(checkBlockQuotes(block('"invented one" and "invented two"', 'src-readme'), SOURCES).map(f => f.quote)).toEqual(['invented one', 'invented two']);
  });

  it('refuses a quote when the block cites no source, or cites only unknown ids', () => {
    expect(kinds('"Tidemark is an in-memory cache."')).toEqual(['quote-without-cited-source']);
    expect(kinds('"Tidemark is an in-memory cache."', 'src-unknown')).toEqual(['quote-without-cited-source']);
  });

  it('handles quotes that contain quotes, straight or curly', () => {
    expect(kinds('The docs say: "The docs say "never block" and then "stop" loudly".', 'src-nested')).toEqual([]);
    expect(kinds('The project states: "The docs say "never block" and then "stop" loudly; he said “quiet “inner” words” too."', 'src-nested')).toEqual([]);
    expect(kinds('He said “quiet “inner” words”.', 'src-nested')).toEqual([]);
    expect(kinds('He said “quiet “invented” words”.', 'src-nested')).toEqual(['quote-not-in-cited-sources']);
    expect(kinds('"never block" and "stop" loudly', 'src-nested')).toEqual([]);
    expect(kinds('"never block" and "stop" loudly and "invented"', 'src-nested')).toEqual(['quote-not-in-cited-sources']);
  });

  it('fails an unterminated, empty or lead-in-only quote rather than skipping it', () => {
    expect(kinds('The text opens "Tidemark is an in-memory cache.', 'src-readme')).toEqual(['unterminated-quote']);
    expect(kinds('He said “Tidemark is an in-memory cache.', 'src-readme')).toEqual(['unterminated-quote']);
    expect(kinds('An empty "" quote.', 'src-readme')).toEqual(['empty-quote']);
    expect(kinds('A blank "  *  " quote.', 'src-readme')).toEqual(['empty-quote']);
    expect(kinds(`${QUOTE_LEAD_IN} Tidemark is an in-memory cache.`, 'src-readme')).toEqual(['lead-in-without-quote']);
    expect(kinds(`${QUOTE_LEAD_IN} "Tidemark is an in-memory cache."`, 'src-readme')).toEqual([]);
    expect(kinds(`${QUOTE_LEAD_IN} "Tidemark is an in-memory cache." Later: ${QUOTE_LEAD_IN} that it is fast.`, 'src-readme')).toEqual(['lead-in-without-quote']);
    expect(kinds(`${QUOTE_LEAD_IN} that it is fast. Later: ${QUOTE_LEAD_IN} "Tidemark is an in-memory cache."`, 'src-readme')).toEqual(['lead-in-without-quote']);
    expect(kinds(`${QUOTE_LEAD_IN}   “Tidemark is an in-memory cache.”`, 'src-readme')).toEqual([]);
  });

  it('leaves text without quotes alone, and does not treat an apostrophe as a quote', () => {
    expect(kinds('The project\'s cache avoids lock contention; it doesn\'t block.', 'src-readme')).toEqual([]);
    expect(kinds('No quotes at all.')).toEqual([]);
  });

  it('truncates a long reported quote and names the block', () => {
    const [finding] = checkBlockQuotes({ id: 'long-block', text: `"${'x'.repeat(500)}"`, sourceIds: ['src-readme'] }, SOURCES);
    expect(finding).toMatchObject({ blockId: 'long-block', kind: 'quote-not-in-cited-sources' });
    expect(finding!.quote).toHaveLength(200);
  });
});

describe('folding forms of a true quotation', () => {
  const FOLD = sourceTextById(files([
    ['src-fold', 'Use `maxmemory` to bound it; it’s “every key” &amp; more. The &lt;b&gt; tag, &#65; and &#x42; and\\_snake\\_case\\*.\n/* one-line comment */\nint SET = 1; // the SET command\n'],
    ['src-close', 'first line\n */ second after the close\n'],
    ['src-under', 'Call active_expire_cycle, then *p = *q, and 2*3*4 and foobar.'],
    ['src-dots', 'He paused and said: wait... what is that?'],
    ['src-dots2', 'He paused and said: wait\u2026 what is that?'],
    ['src-digits', 'The default port is 6379 for Redis.'],
    ['src-ellipsis', 'Redis evicts keys when memory is full, using an approximate LRU that samples a few keys, and then removes the best candidate.'],
  ]));
  const run = (text: string, ...ids: string[]) => checkBlockQuotes(block(text, ...ids), FOLD).map(f => f.kind);
  it('ignores backticks, curly apostrophes, entities and backslash escapes on both sides', () => {
    expect(run('Use "maxmemory" to bound it', 'src-fold')).toEqual([]);
    expect(run('Use "`maxmemory`" to bound it', 'src-fold')).toEqual([]);
    expect(run('It says "it\'s “every key”" here', 'src-fold')).toEqual([]);
    expect(run('It says "& more. The <b> tag"', 'src-fold')).toEqual([]);
    expect(run('It says "The <b> tag, A and B"', 'src-fold')).toEqual([]);
    expect(run('It says "and_snake_case*"', 'src-fold')).toEqual([]);
  });
  it('folds a straight-quoted reading of a curly-quoted source, a comment close at a line start, and a code span inside a quote', () => {
    expect(run('It says "it\'s "every key" & more"', 'src-fold')).toEqual([]);
    expect(run('It says "Use maxmemory to bound it"', 'src-fold')).toEqual([]);
    expect(run('It says "second after the close"', 'src-close')).toEqual([]);
    expect(normaliseForQuote(' */ second after the close')).toBe('second after the close');
  });
  it('treats digits as word characters at a boundary', () => {
    expect(run('The port "6379" is used', 'src-digits')).toEqual([]);
    expect(run('The port "637" is used', 'src-digits')).toEqual(['quote-not-in-cited-sources']);
    expect(run('The port "379" is used', 'src-digits')).toEqual(['quote-not-in-cited-sources']);
  });
  it('leaves no stray slash from a same-line block-comment close', () => {
    expect(normaliseForQuote('/* one-line comment */')).toBe('one-line comment');
    expect(run('It says "one-line comment"', 'src-fold')).toEqual([]);
    expect(run('It says "the SET command"', 'src-fold')).toEqual([]);
  });
  it('does not allow elision: an ellipsis, bracketed or not, is an elided-quote unless the source has it at that spot', () => {
    expect(run('"Redis evicts keys ... removes the best candidate"', 'src-ellipsis')).toEqual(['elided-quote']);
    expect(run('"Redis evicts keys [...] samples a few keys"', 'src-ellipsis')).toEqual(['elided-quote']);
    expect(run('"Redis evicts keys [\u2026] samples a few keys"', 'src-ellipsis')).toEqual(['elided-quote']);
    expect(run('"Redis evicts keys, \u2026 samples"', 'src-ellipsis')).toEqual(['elided-quote']);
    expect(run('"wait... what"', 'src-dots')).toEqual([]);
    expect(run('"wait \u2026 what"', 'src-dots')).toEqual(['elided-quote']);
    expect(run('"invented words ..."', 'src-dots')).toEqual(['elided-quote']);
    expect(run('"invented words"', 'src-dots')).toEqual(['quote-not-in-cited-sources']);
  });
  it('folds the ellipsis character and three periods to one form on both sides', () => {
    expect(normaliseForQuote('wait\u2026 what')).toBe('wait... what');
    expect(run('"wait\u2026 what"', 'src-dots')).toEqual([]);
    expect(run('"wait... what"', 'src-dots2')).toEqual([]);
  });
  it('never joins two sources into one quotation', () => {
    expect(run('"The default port is 6379 for Redis. Redis evicts keys"', 'src-digits', 'src-ellipsis')).toEqual(['quote-not-in-cited-sources']);
  });
  it('drops * and _ only as paired emphasis at word edges, never inside an identifier or an unpaired pointer', () => {
    expect(normaliseForQuote('a **bold** and __b__ and _em_ and *x* and ***both***')).toBe('a bold and b and em and x and both');
    expect(normaliseForQuote('active_expire_cycle and *p = *q and 2*3*4')).toBe('active_expire_cycle and *p = *q and 2*3*4');
    expect(normaliseForQuote('snake_case_ and x_y_ z')).toBe('snake_case_ and x_y_ z');
    expect(normaliseForQuote('x *p\nq* y')).toBe('x *p q* y');
    expect(run('"active_expire_cycle"', 'src-under')).toEqual([]);
    expect(run('"active expire cycle"', 'src-under')).toEqual(['quote-not-in-cited-sources']);
    expect(run('"activeexpirecycle"', 'src-under')).toEqual(['quote-not-in-cited-sources']);
    expect(run('"foo_bar"', 'src-under')).toEqual(['quote-not-in-cited-sources']);
    expect(run('"then *p = *q, and 2*3*4"', 'src-under')).toEqual([]);
    expect(run('"then p = q, and 234"', 'src-under')).toEqual(['quote-not-in-cited-sources']);
  });
  it('matches only on word boundaries', () => {
    expect(run('The term "ed" appears', 'src-ellipsis')).toEqual(['quote-not-in-cited-sources']);
    expect(run('The term "Redis" appears', 'src-ellipsis')).toEqual([]);
    expect(run('The term "LRU" appears', 'src-ellipsis')).toEqual([]);
    expect(run('The term "RU" appears', 'src-ellipsis')).toEqual(['quote-not-in-cited-sources']);
    expect(run('The term "Redi" appears', 'src-ellipsis')).toEqual(['quote-not-in-cited-sources']);
  });
});

describe('a file split into pieces', () => {
  const lines = Array.from({ length: 6000 }, (_, i) => `line ${i} of the long file`).join('\n');
  const body = `${lines}\nThe boundary quote crosses`;
  const pieces = files([['long', `${body} the piece edge and continues.\n${'padding line\n'.repeat(5000)}`]]);
  it('groups pieces per file: two files with identical bodies at different paths each keep their own pieces', () => {
    const twin = files([['long-a', body + ' the piece edge and continues.\n' + 'padding line\n'.repeat(5000)], ['long-b', body + ' the piece edge and continues.\n' + 'padding line\n'.repeat(5000)]]);
    const texts = sourceTextById(twin);
    const first = twin.find(piece => piece.sourceId.startsWith('long-a'))!;
    const edge = first.spans[0]!.text.length;
    const whole = twin.filter(piece => piece.sourceId.startsWith('long-a')).map(piece => piece.spans[0]!.text).join('');
    const crossing = whole.slice(edge - 20, edge + 20).replace(/\s+/gu, ' ').trim().split(' ').slice(1, -1).join(' ');
    expect(checkBlockQuotes({ id: 'b', text: `"${crossing}"`, sourceIds: [first.sourceId] }, texts)).toEqual([]);
  });
  it('checks a block against the whole file, so a quote may cross a piece boundary', () => {
    expect(pieces.length).toBeGreaterThan(1);
    const texts = sourceTextById(pieces);
    const edge = pieces[0]!.spans[0]!.text.length;
    const whole = pieces.map(piece => piece.spans[0]!.text).join('');
    const crossing = whole.slice(edge - 20, edge + 20).replace(/\s+/gu, ' ').trim();
    expect(checkBlockQuotes({ id: 'b', text: `"${crossing.split(' ').slice(1, -1).join(' ')}"`, sourceIds: [pieces[0]!.sourceId] }, texts)).toEqual([]);
    expect(checkBlockQuotes({ id: 'b', text: `"${crossing.split(' ').slice(1, -1).join(' ')}"`, sourceIds: [pieces[1]!.sourceId] }, texts)).toEqual([]);
    expect(checkBlockQuotes({ id: 'b', text: '"not anywhere in the long file"', sourceIds: [pieces[0]!.sourceId] }, texts).map(f => f.kind)).toEqual(['quote-not-in-cited-sources']);
  });
});

describe('a deferred tail of a split file', () => {
  const lines = Array.from({ length: 6000 }, (_, i) => `line ${i} of the long file`).join('\n');
  const pieces = files([['long', `${lines}\nThe boundary quote crosses the piece edge and continues.\n${'padding line\n'.repeat(5000)}\nTail only words here.\n`]]);
  const last = pieces.at(-1)!;
  it('checks against the pieces that are present, joined from the first: a prefix keeps its cross-piece quotes and loses the unread tail', () => {
    expect(pieces.length).toBeGreaterThanOrEqual(3);
    const prefix = pieces.slice(0, 2);
    const { body: _b, segment: _s, spans: _p, ...bound } = pieces[2]!;
    const deferredRow: GenerationSource = { ...bound, sourceId: `s-${'a'.repeat(24)}`, exclusion: { excluded: true, reason: 'deferred-by-budget' }, spans: [] };
    const texts = sourceTextById([...prefix, deferredRow]);
    const edge = pieces[0]!.spans[0]!.text.length;
    const crossing = (prefix[0]!.spans[0]!.text + prefix[1]!.spans[0]!.text).slice(edge - 20, edge + 20).replace(/\s+/gu, ' ').trim().split(' ').slice(1, -1).join(' ');
    expect(checkBlockQuotes({ id: 'b', text: `"${crossing}"`, sourceIds: [prefix[0]!.sourceId] }, texts)).toEqual([]);
    expect(checkBlockQuotes({ id: 'b', text: '"Tail only words here."', sourceIds: [prefix[0]!.sourceId] }, texts).map(f => f.kind)).toEqual(['quote-not-in-cited-sources']);
    expect(checkBlockQuotes({ id: 'b', text: '"Tail only words here."', sourceIds: [last.sourceId] }, sourceTextById(pieces)).map(f => f.kind)).toEqual([]);
  });
});

describe('inspectBlockQuotes', () => {
  it('counts the quoted spans, so a block with no quotes is distinguishable from one whose quotes verified', () => {
    expect(inspectBlockQuotes(block('No quotation marks here', 'src-readme'), SOURCES)).toEqual({ quotes: 0, findings: [] });
    expect(inspectBlockQuotes(block('He said "in-memory cache" and "event loop"', 'src-readme'), SOURCES)).toEqual({ quotes: 2, findings: [] });
  });
});

describe('the repair finding', () => {
  it('asks for a verbatim quotation or an Inferred sentence, and never for rewording that contradicts the repair prompt', () => {
    const { message } = quoteFindingAsReviewFinding({ blockId: 'b', kind: 'quote-not-in-cited-sources', quote: 'x' });
    expect(message).toContain('Give one quotation per lead-in, and quote it verbatim from a cited source, or remove the quotation marks and mark the sentence Inferred.');
    expect(message).not.toContain('own words');
    expect(quoteFindingAsReviewFinding({ blockId: 'b', kind: 'elided-quote', quote: 'a ... b' }).message).toContain('elides text with an ellipsis, which is not allowed');
  });
});

describe('a quotation after the lead-in', () => {
  const lead = (rest: string, ...ids: string[]) => checkBlockQuotes(block(`${QUOTE_LEAD_IN} ${rest}`, ...ids), SOURCES).map(f => f.kind);
  it('is the exact lead-in the dossier prompts use', () => {
    expect(QUOTE_LEAD_IN).toBe('The project states:');
    expect(QUOTE_LEAD_IN.includes("'")).toBe(false);
  });
  it('runs to the last straight quote before the next lead-in, so it may contain quotes', () => {
    expect(lead('"The docs say "never block" and then "stop" loudly"', 'src-nested')).toEqual([]);
    expect(lead('"The docs say "never block" and then "stop" loudly". ' + QUOTE_LEAD_IN + ' "in-memory cache"', 'src-nested', 'src-readme')).toEqual([]);
    expect(lead('"The docs say "never block" and then "stop" loudly". ' + QUOTE_LEAD_IN + ' "not in any source"', 'src-nested', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
    expect(checkBlockQuotes(block(`${QUOTE_LEAD_IN} "in-memory cache" ${QUOTE_LEAD_IN} "event loop"`, 'src-readme'), SOURCES)).toEqual([]);
  });
  it('refuses a matching opening with an unverified tail', () => {
    expect(lead('"The docs say "never block" and then "stop" loudly; he said "bogus tail"', 'src-nested')).toEqual(['quote-not-in-cited-sources']);
    expect(lead('"in-memory cache and then some invented words"', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
  });
  it('refuses a stray double quote in the prose after the quotation, and a second quoted term after it', () => {
    expect(lead('"in-memory cache" and a stray " in prose', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
    expect(lead('"in-memory cache". It uses "event loop" too.', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
  });
  it('fails a lead-in with no quotation mark, an unterminated one, and an empty one', () => {
    expect(lead('that it is fast', 'src-readme')).toEqual(['lead-in-without-quote']);
    expect(lead('"in-memory cache', 'src-readme')).toEqual(['unterminated-quote']);
    expect(lead('""', 'src-readme')).toEqual(['empty-quote']);
  });
  it('still checks quotes outside a lead-in quotation', () => {
    expect(checkBlockQuotes(block(`He wrote "bogus" first. ${QUOTE_LEAD_IN} "in-memory cache"`, 'src-readme'), SOURCES).map(f => f.quote)).toEqual(['bogus']);
  });
});

describe('the cases the retired quotations.ts held, now enforced by this checker', () => {
  const SRC = sourceTextById(files([['src-brindle', 'Brindle is **fast**.\nIt reads [the content directory](docs/content.md) and calls it "the tree".']]));
  const quote = (text: string): string => `The project states: "${text}"`;
  const ok = (text: string, ...ids: string[]): boolean => checkBlockQuotes(block(text, ...(ids.length === 0 ? ['src-brindle'] : ids)), SRC).length === 0;
  it.each([
    ['an exact quotation', quote('Brindle is **fast**.')],
    ['a quotation across the source line break', quote('Brindle is fast. It reads the content directory')],
    ['a quotation with the link syntax kept', quote('It reads [the content directory](docs/content.md)')],
    ['a quotation that itself contains double quotes', quote('and calls it "the tree".')],
    ['two quotations in one text', `${quote('Brindle is fast.')} Also, ${quote('It reads the content directory')}`],
    ['text with no quotation', 'Brindle reads the content directory.'],
  ])('accepts %s', (_name, text) => { expect(ok(text)).toBe(true); });
  it.each([
    ['a changed word', quote('Brindle is quick.')],
    ['a changed case', quote('brindle is fast.')],
    ['dropped punctuation', quote('Brindle is fast It reads')],
    ['an added word', quote('Brindle is very fast.')],
    ['an empty quotation', quote('')],
    ['an unterminated quotation', 'The project states: "Brindle is fast.'],
    ['a second quotation that does not match', `${quote('Brindle is fast.')} Also, ${quote('It writes the tree.')}`],
    ['a quotation spliced from two places', quote('Brindle is fast. It calls it "the tree".')],
    ['a matching opening with an unverified tail after an inner quote', quote('It reads the content directory and calls it "the tree" and "the root".')],
    ['a quotation followed by prose that contains a double quote', `${quote('Brindle is fast.')} Its "speed" is not quantified.`],
  ])('refuses %s', (_name, text) => { expect(ok(text)).toBe(false); });
  it('matches within one source, never across two', () => {
    const two = sourceTextById(files([['one', 'one'], ['two', 'two']]));
    expect(checkBlockQuotes(block(quote('one two'), 'one', 'two'), two).map(f => f.kind)).toEqual(['quote-not-in-cited-sources']);
    expect(checkBlockQuotes(block(quote('two'), 'one', 'two'), two)).toEqual([]);
  });
});
