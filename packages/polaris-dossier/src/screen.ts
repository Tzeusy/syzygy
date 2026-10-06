import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { POLICY_PATH, readPolicyActChain } from '@syzygy/polaris-generation-consent';
import { compileDetectors, deniedPathReason, detectSecrets, scanActiveContent, type DeniedPathRules, type SecretDetector } from '@syzygy/three-surface-poc-core';

/** Classification and screening of every blob Syzygy reads for a check (REQ-polaris-generation-033: "every object SHALL be classified
 * and screened under the observing project's effective policies (REQ-polaris-generation-025) before its content is used in a check").
 *
 * The policy is the one the screening-scope act chain puts in force now, its bytes hashed against the chain's digest at load, so a policy
 * edited between the step's gate and this read is refused, not used. The rules are the any-repo reader's
 * (`apps/three-surface-poc/src/polaris-generation/public-source-screening.ts`), unforked: a path is excluded unread when a denied-path
 * rule names it, when a secret detector matches the path itself, or when its final segment ends with none of the scope's code-content
 * `sourceExtensions`; a body that is not UTF-8 text, that a secret detector matches, or that holds active content is excluded after the
 * read. An excluded blob is never used to verify a quotation, and no finding carries its bytes. Policy residual, not repaired here: the
 * detectors match literal forms only, so an encoded or split secret passes them.
 *
 * TODO(syzygy-qkea.17): these rules are a copy of the app's; move them into one shared package that both import. Until then
 * `screen.test.ts` builds both screens from the same policy and fails if they disagree on any path or body of its population. */

export type ScreenExclusion = 'denied-path' | 'secret-detector-match' | 'unknown-extraction-class' | 'not-utf8-text' | 'active-content';

export interface DossierScreen {
  readonly policyId: string;
  readonly policyVersion: string;
  readonly policySha256: string;
  /** Why a path is excluded before any read, or undefined when its blob may be read. */
  readonly screenPath: (repositoryPath: string) => ScreenExclusion | undefined;
  /** Why a read body is excluded, or undefined when it is admitted. */
  readonly screenBody: (body: string) => ScreenExclusion | undefined;
}

export type ScreenLoad = { readonly ok: true; readonly screen: DossierScreen } | { readonly ok: false; readonly why: string };

const stringList = (value: unknown): value is readonly string[] => Array.isArray(value) && value.every((item) => typeof item === 'string' && item.length > 0);
const isObject = (value: unknown): value is Readonly<Record<string, unknown>> => value !== null && typeof value === 'object' && !Array.isArray(value);

/** Build the screen from the policy's bytes. Every field the rules need must be present and well formed, or the screen is refused. */
export function buildDossierScreen(policy: Uint8Array): ScreenLoad {
  const refuse = (why: string): ScreenLoad => ({ ok: false, why: `the screening policy cannot be applied: ${why}` });
  let doc: unknown;
  try { doc = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(policy)); } catch { return refuse('it is not UTF-8 JSON'); }
  if (!isObject(doc) || typeof doc['policyId'] !== 'string' || typeof doc['policyVersion'] !== 'string') return refuse('its identity is unreadable');
  const scope = doc['publicSourceScope'], admission = doc['sourceAdmission'];
  if (!isObject(scope)) return refuse('it carries no publicSourceScope');
  if (!isObject(admission) || !stringList(admission['deniedPathBasenames']) || !stringList(admission['deniedPathPrefixes']) || !stringList(admission['deniedPathSuffixes'])) {
    return refuse('its denied-path rules are unreadable');
  }
  const classification = scope['contentClassification'];
  const rules = isObject(classification) && Array.isArray(classification['rules']) ? classification['rules'] : [];
  const codeContent = rules.filter((rule: unknown) => isObject(rule) && rule['class'] === 'code-content');
  const extensions = isObject(codeContent[0]) ? codeContent[0]['sourceExtensions'] : undefined;
  if (codeContent.length !== 1 || !stringList(extensions) || extensions.length === 0 || extensions.some((extension) => !/^\.[^/\s]+$/u.test(extension) || extension.includes('..'))) {
    return refuse('its code-content sourceExtensions are unreadable');
  }
  const denied: DeniedPathRules = { basenames: admission['deniedPathBasenames'], prefixes: admission['deniedPathPrefixes'], suffixes: admission['deniedPathSuffixes'] };
  let detectors: ReturnType<typeof compileDetectors>;
  try { detectors = compileDetectors({ detectors: doc['detectors'] as readonly SecretDetector[] }); } catch (error) { return refuse(`its detectors do not compile (${error instanceof Error ? error.message : 'invalid'})`); }
  return {
    ok: true,
    screen: {
      policyId: doc['policyId'], policyVersion: doc['policyVersion'], policySha256: createHash('sha256').update(policy).digest('hex'),
      screenPath: (repositoryPath) => deniedPathReason(repositoryPath, denied) !== undefined ? 'denied-path'
        : detectSecrets(detectors, repositoryPath) !== undefined ? 'secret-detector-match'
          : extensions.some((extension) => (repositoryPath.split('/').at(-1) ?? '').endsWith(extension)) ? undefined : 'unknown-extraction-class',
      screenBody: (body) => detectSecrets(detectors, body) !== undefined ? 'secret-detector-match' : scanActiveContent(body).length > 0 ? 'active-content' : undefined,
    },
  };
}

/** The screen of the policy in force at `now`, from a Syzygy checkout: the act chain must put an act in force whose argument is the
 * policy's current bytes, and the bytes read for the screen must hash to that argument. */
export async function loadDossierScreen(root: string, now: number, readBytes: (file: string) => Buffer = (file) => fs.readFileSync(file)): Promise<ScreenLoad> {
  const chain = await readPolicyActChain({ root, now });
  if (chain.state !== 'ok') return { ok: false, why: `no screening policy is in force: ${chain.why}` };
  // The chain read the policy once; this is a second read, so a change between the two is caught here.
  let bytes: Buffer;
  try { bytes = readBytes(path.join(root, POLICY_PATH)); } catch (cause) {
    return { ok: false, why: `the screening policy cannot be read (${(cause as NodeJS.ErrnoException).code ?? 'unknown-error'})` };
  }
  if (createHash('sha256').update(bytes).digest('hex') !== chain.final.digest) return { ok: false, why: 'the screening policy changed after its act was checked; its bytes differ from the act\'s argument' };
  return buildDossierScreen(new Uint8Array(bytes));
}
