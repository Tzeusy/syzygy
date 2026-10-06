import * as fs from 'node:fs';
import * as path from 'node:path';
import { providerStatementGate, type GateSources } from './gate-sources.js';
import { readRunRecord, type RecordedRunConfig } from './run-record.js';
import { RUN_LAYOUT } from './state-directory.js';

/** The step guard every later command calls before it reads an object for the run (REQ-polaris-generation-033: "At every later
 * check, review check and render, Syzygy SHALL verify again that the recorded pinned revision is a revision the in-force observation
 * consent names, and SHALL refuse the step otherwise").
 *
 * The recorded pin is read from `run.json`, which the agent sessions can write, so which revision the run was pinned to is Inferred;
 * that the revision is consented is verified here, at this step, against the records in force now. Every gate is re-read: the
 * consent found by the URL must still be the one for the recorded repository and must still name the pinned commit; the registry
 * entry and the policy must still be in force by their acts; a statement the run relied on must still be in force and the same one.
 * HEAD is never read again: later steps read the pinned revision only. Every failing reason is reported, not only the first. */

export type ReverifyResult =
  | { readonly ok: true; readonly record: RecordedRunConfig; readonly consentRecord: string }
  | { readonly ok: false; readonly reasons: readonly string[] };

export async function reverifyPinnedRevision(runDir: string, sources: GateSources, now: number): Promise<ReverifyResult> {
  let text: string;
  try {
    text = fs.readFileSync(path.join(path.resolve(runDir), RUN_LAYOUT.config), 'utf8');
  } catch (cause) {
    return { ok: false, reasons: [`${runDir} holds no readable ${RUN_LAYOUT.config} (${(cause as NodeJS.ErrnoException).code ?? 'unknown-error'})`] };
  }
  const read = readRunRecord(text);
  if (!read.ok) return { ok: false, reasons: [read.detail] };
  const { subject, declared } = read.record;
  const { repositoryId, url } = subject.repository;
  const commit = subject.pinnedRevision.commit;

  const reasons: string[] = [];
  const ids = await sources.repositoryIdsFor(url);
  if (ids.length !== 1 || ids[0] !== repositoryId) {
    reasons.push(`the observation consents in force for ${url} are [${ids.join(', ')}], not exactly the recorded ${repositoryId}: the consent was withdrawn, superseded or is ambiguous`);
  }
  const consent = await sources.observationConsentFor(repositoryId, commit);
  if (!consent.satisfied) reasons.push(`the recorded pinned revision ${commit} is not a revision the in-force observation consent for ${repositoryId} names: ${consent.why}`);
  const [registryEntry, screeningPolicy] = await Promise.all([sources.registryEntry(), sources.screeningPolicy()]);
  if (registryEntry.state !== 'ok') reasons.push(`the source-acquisition registry entry is no longer in force: ${registryEntry.why}`);
  if (screeningPolicy.state !== 'ok') reasons.push(`the classification and screening policy is no longer in force: ${screeningPolicy.why}`);
  if (subject.providerStatement !== null) {
    const statement = providerStatementGate(await sources.providerStatements.statementsFor(repositoryId), declared.agentProvider, now);
    if (statement.state !== 'ok') reasons.push(`the per-project statement ${subject.providerStatement} the run relies on is no longer in force: ${statement.why}`);
    else if (statement.record !== subject.providerStatement) reasons.push(`the in-force per-project statement is ${statement.record}, not the ${subject.providerStatement} the run relies on`);
  }
  if (reasons.length > 0 || !consent.satisfied) return { ok: false, reasons };
  return { ok: true, record: read.record, consentRecord: consent.record };
}
