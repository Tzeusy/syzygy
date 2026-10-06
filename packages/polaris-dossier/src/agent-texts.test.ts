import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';
import { DOSSIER_USAGE } from './cli.js';

/** The lint over the installed agent texts (syzygy-qkea.12; REQ-polaris-generation-033 and 035; D9-N5; R3-F9): the Claude Code skill
 * and the Codex instructions. Neither grants execution: each defers to the execution rule in the run's `brief.md` and, absent it, says
 * the observed project is not built or run outside an explicit, opt-in execution profile. `allow-execution` appears only as a command
 * the operator types personally, beside the instruction never to run it. Every `syzygy dossier` command they name exists, with the
 * options and literal arguments its usage states and every option its usage requires. The skill's description names any repository
 * the operator holds the consents for, not only public ones. Each predicate is shown to fire on a mutated copy of the text. */

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const TEXTS = ['.claude/skills/polaris-dossier/SKILL.md', '.codex/skills/polaris-dossier/SKILL.md'];

interface Synopsis { readonly positional: readonly string[]; readonly required: ReadonlySet<string>; readonly options: ReadonlyMap<string, readonly string[] | null> }

/** Each command's synopsis from the usage text: positional words (literal alternatives split on `|`, placeholders kept as `<…>`), every
 * option with its literal value alternatives (null for a placeholder value), and which options are required (outside brackets). */
function synopses(usage: string): ReadonlyMap<string, Synopsis> {
  const out = new Map<string, Synopsis>();
  for (const line of usage.split('\n')) {
    const match = /^ {2}([a-z][a-z-]*)((?: \S+)*?)(?: {2,}.*)?$/u.exec(line);
    if (match === null || match[1] === 'help') continue;
    const tokens = (match[2] ?? '').trim().split(/ +/u).filter((token) => token !== '');
    const positional: string[] = [];
    const required = new Set<string>();
    const options = new Map<string, readonly string[] | null>();
    let depth = 0;
    for (let i = 0; i < tokens.length; i++) {
      const raw = tokens[i]!;
      const opens = raw.startsWith('[');
      const token = raw.replace(/^\[|\]$/gu, '');
      if (opens) depth++;
      if (token.startsWith('--')) {
        const value = tokens[i + 1]?.replace(/\]$/u, '');
        const closesOnValue = tokens[i + 1]?.endsWith(']') ?? false;
        options.set(token, value === undefined || value.startsWith('<') ? null : value.split(/[|,]/u));
        if (depth === 0) required.add(token);
        i++;
        if (raw.endsWith(']') || closesOnValue) depth = Math.max(0, depth - 1);
        continue;
      }
      if (depth === 0) positional.push(token);
      if (raw.endsWith(']')) depth = Math.max(0, depth - 1);
    }
    out.set(match[1]!, { positional, required, options });
  }
  return out;
}
const SYNOPSES = synopses(DOSSIER_USAGE);

/** The code spans of a Markdown text, whitespace normalised; a span may cross a line break inside a paragraph. */
const codeSpans = (text: string): string[] => [...text.matchAll(/`([^`]+)`/gu)].map((match) => match[1]!.replace(/\s+/gu, ' ').trim());

/** Faults in the `syzygy dossier` commands a text names. */
function commandFaults(text: string): string[] {
  const faults: string[] = [];
  for (const span of codeSpans(text).filter((candidate) => candidate.startsWith('syzygy dossier '))) {
    const [, , command, ...args] = span.split(' ');
    const synopsis = command === undefined ? undefined : SYNOPSES.get(command);
    if (synopsis === undefined) { faults.push(`${span}: no such command`); continue; }
    const used = new Set<string>();
    const positional: string[] = [];
    for (let i = 0; i < args.length; i++) {
      const arg = args[i]!;
      if (!arg.startsWith('--')) { positional.push(arg); continue; }
      if (!synopsis.options.has(arg)) { faults.push(`${span}: ${command} takes no ${arg}`); i++; continue; }
      used.add(arg);
      const value = args[i + 1];
      i++;
      const allowed = synopsis.options.get(arg)!;
      if (allowed !== null && value !== undefined && !value.startsWith('<') && !value.split(/[|,]/u).every((part) => allowed.includes(part))) faults.push(`${span}: ${arg} takes ${allowed.join('|')}, not ${value}`);
    }
    for (const flag of synopsis.required) if (!used.has(flag)) faults.push(`${span}: ${command} requires ${flag}`);
    if (positional.length !== synopsis.positional.length) { faults.push(`${span}: ${command} takes ${synopsis.positional.length} positional argument(s), not ${positional.length}`); continue; }
    positional.forEach((word, index) => {
      const expected = synopsis.positional[index]!;
      if (expected.startsWith('<') || word.startsWith('<')) return;
      if (!word.split('|').every((part) => expected.split('|').includes(part))) faults.push(`${span}: ${word} is not one of ${expected}`);
    });
  }
  return faults;
}

/** The text's blocks: paragraphs and list items, each whitespace normalised. */
const blocks = (text: string): string[] => text.split(/\n\s*\n|\n(?=\s*(?:-|\d+\.) )/u).map((block) => block.replace(/\s+/gu, ' ').trim()).filter((block) => block !== '');
const sentences = (block: string): string[] => block.replace(/`[^`]*`/gu, (span) => span.replace(/[.;]/gu, ' ')).split(/(?<=[.;!?])\s+/u);

/** Sentences that grant building or running the observed project: a permissive verb with an execution verb and no negation or
 * deferral to the brief. */
function grantingSentences(text: string): string[] {
  const permission = /\b(?:you may|you can|may|can|are (?:allowed|permitted|free) to|feel free to|go ahead and|it is fine to|you should|you must)\b/iu;
  const execution = /\b(?:build|run|execute|compile|install|test)\b/iu;
  const negation = /\b(?:not|never|no|nothing|unless|only)\b|brief\.md|execution rule/iu;
  return blocks(text).flatMap(sentences).filter((sentence) => permission.test(sentence) && execution.test(sentence) && !negation.test(sentence));
}

/** Blocks naming `allow-execution` that do not make it the operator's to type personally, beside the instruction never to run it. */
function allowExecutionFaults(text: string): string[] {
  return blocks(text).filter((block) => block.includes('allow-execution'))
    .filter((block) => !/\bthe operator (?:types|to type)\b/u.test(block) || !/\bpersonally\b/u.test(block) || !/\bnever run (?:that command|it) yourself\b/iu.test(block));
}

const frontmatter = (text: string): Record<string, string> => Object.fromEntries((/^---\n([\s\S]*?)\n---\n/u.exec(text)?.[1] ?? '').split('\n').flatMap((line) => {
  const match = /^([a-z]+): (.*)$/u.exec(line);
  return match === null ? [] : [[match[1]!, match[2]!]];
}));

function descriptionFaults(text: string): string[] {
  const description = frontmatter(text)['description'] ?? '';
  const faults: string[] = [];
  if (!description.includes('any repository the operator holds the consents for')) faults.push('the description does not name any repository the operator holds the consents for');
  if (/\bpublic\b/iu.test(description)) faults.push('the description restricts itself to public repositories');
  return faults;
}

function deferralFaults(text: string): string[] {
  const flat = text.replace(/\s+/gu, ' ');
  const faults: string[] = [];
  if (!/Follow the execution rule in the run's `brief\.md`/u.test(flat)) faults.push('the text does not defer to the execution rule in the run\'s brief.md');
  if (!/not to be built or run outside an explicit, opt-in execution profile/u.test(flat)) faults.push('the text does not say, absent the brief, that the project is not built or run outside an explicit, opt-in execution profile');
  return faults;
}

const lint = (text: string): string[] => [...commandFaults(text), ...grantingSentences(text).map((s) => `grants execution: ${s}`), ...allowExecutionFaults(text).map((b) => `allow-execution not the operator's: ${b}`), ...descriptionFaults(text), ...deferralFaults(text)];

describe('agent texts (S11)', () => {
  it('reads every command synopsis from the usage text', () => {
    expect([...SYNOPSES.keys()].sort()).toEqual(['allow-execution', 'brief', 'check', 'close', 'init', 'inventory-brief', 'inventory-check', 'launch-form', 'preflight', 'render', 'review-check', 'review-packet', 'session-prompt', 'status']);
    expect(SYNOPSES.get('init')).toEqual({ positional: ['<clone>'], required: new Set(['--url', '--config']), options: new Map([['--url', null], ['--config', null], ['--state-root', null]]) });
    expect(SYNOPSES.get('launch-form')!.positional).toEqual(['<run>', 'inventory|review', 'terminal|bang']);
    expect(SYNOPSES.get('allow-execution')!.required).toEqual(new Set(['--revision', '--declare']));
    expect(SYNOPSES.get('review-check')!.options.get('--kind')).toEqual(['fidelity', 'design']);
  });

  for (const file of TEXTS) {
    it(`${file} passes the lint`, () => {
      const text = fs.readFileSync(path.join(ROOT, file), 'utf8');
      expect(codeSpans(text).filter((span) => span.startsWith('syzygy dossier ')).length).toBeGreaterThan(10);
      expect(lint(text)).toEqual([]);
    });
  }

  it('each predicate fires on a mutated copy of the skill', () => {
    const text = fs.readFileSync(path.join(ROOT, TEXTS[0]!), 'utf8');
    const swap = (from: string, to: string): string => { expect(text.includes(from)).toBe(true); return text.replace(from, to); };
    expect(grantingSentences(`${text}\nYou may build and run the project to confirm a claim.\n`)).toEqual(['You may build and run the project to confirm a claim.']);
    expect(commandFaults(swap('`syzygy dossier check <run>`', '`syzygy dossier verify <run>`'))).toEqual(['syzygy dossier verify <run>: no such command']);
    expect(commandFaults(swap('`syzygy dossier check <run>`', '`syzygy dossier check <run> --strict x`'))).toEqual(['syzygy dossier check <run> --strict x: check takes no --strict']);
    expect(commandFaults(swap('`syzygy dossier init <clone> --url <url> --config <file> --state-root <dir>`', '`syzygy dossier init <clone> --url <url>`'))).toEqual(['syzygy dossier init <clone> --url <url>: init requires --config']);
    expect(commandFaults(swap('`syzygy dossier session-prompt <run> inventory`', '`syzygy dossier session-prompt <run> authoring`'))).toEqual(['syzygy dossier session-prompt <run> authoring: authoring is not one of inventory|review']);
    expect(commandFaults(swap('--kind fidelity|design --verdict verdict.json', '--kind summary --verdict verdict.json'))).toHaveLength(1);
    expect(allowExecutionFaults(swap('Never\n   run that command yourself', 'Run\n   that command yourself'))).toHaveLength(1);
    expect(descriptionFaults(swap('for any repository the operator holds the consents for', 'for any public repository'))).toHaveLength(2);
    expect(deferralFaults(swap('Follow the execution rule in the run\'s `brief.md`', 'Use your judgement'))).toHaveLength(1);
  });
});
