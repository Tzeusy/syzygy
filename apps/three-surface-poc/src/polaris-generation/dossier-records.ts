import { createHash } from 'node:crypto';
import { readFile, readdir } from 'node:fs/promises';
import path from 'node:path';

import { INSTANCES_DIR, createPackageAdmissionReader, createPackageAdmissionRecordsPort, inForceRecords, type PackageReaderFs } from '@syzygy/polaris-generation-consent';

import type { AdmissionRecordsPort, AdmissionRequirement } from './dossier-trigger.js';

/** The egress record in force for a requirement, with the digest of its exact bytes. */
export interface InForceEgress { readonly record: string; readonly digest: string }

/** The trigger's records port plus the one question stage authorisation needs. */
export interface WiredRecordsPort extends AdmissionRecordsPort {
  /** One fresh read: the single in-force Anthropic egress record that lists this repository, or null (none, several, or unreadable). */
  readonly inForceEgress: (requirement: AdmissionRequirement) => Promise<InForceEgress | null>;
}

const OBSERVATION_FILE = 'OBSERVATION-CONSENT.md';
const CONSENTING_PROJECT = 'project:syzygy';
const nodeFs: PackageReaderFs = { readdir: dir => readdir(dir), readFile: file => readFile(file, 'utf8') };
const sha256 = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');

/** `https://github.com/<owner>/<repo>` with nothing after the repository name. */
export const CANONICAL_UPSTREAM = /^https:\/\/github\.com\/[A-Za-z0-9][A-Za-z0-9-]{0,38}\/[A-Za-z0-9._-]{1,100}$/u;

/**
 * Records for `poc:dossier`, built from the package readers over a Syzygy
 * checkout. `repositoryIdsFor(url)` returns the id of every observation record
 * that is in force now, whose instance bytes are exactly the bytes its act
 * bound, and whose single `Upstream:` line is exactly `url`. The id is never
 * derived from the URL: two repositories can share a spelling, and one repo's
 * consent must not apply to another. The `Upstream:` line says it is
 * "configuration, not repository identity"; it is read here only to find which
 * owner-consented record to ask, and the consent itself is still checked by
 * `check()` against that record's id and the pinned commit.
 */
export function createWiredRecordsPort(options: { readonly root: string; readonly now: () => number; readonly fs?: PackageReaderFs }): WiredRecordsPort {
  const fs = options.fs ?? nodeFs;
  const fsOption = options.fs === undefined ? {} : { fs: options.fs };
  const base = createPackageAdmissionRecordsPort({ root: options.root, now: options.now, ...fsOption });
  const reader = createPackageAdmissionReader({ root: options.root, ...fsOption });
  return {
    source: base.source,
    check: requirement => base.check(requirement as AdmissionRequirement & Record<string, unknown>),
    repositoryIdsFor: async url => {
      if (typeof url !== 'string' || !CANONICAL_UPSTREAM.test(url)) return [];
      try {
        const live = inForceRecords(await reader.read(), options.now()).filter(r => r.class === 'observation' && r.project === CONSENTING_PROJECT && r.repositoryId !== null);
        if (live.length === 0) return [];
        const dir = path.join(options.root, INSTANCES_DIR);
        const found = new Set<string>();
        for (const name of [...await fs.readdir(dir)].sort()) {
          let text: string;
          try { text = await fs.readFile(path.join(dir, name, OBSERVATION_FILE)); } catch { continue; }   // a directory without an observation record
          const upstream = [...text.matchAll(/^Upstream: (\S+)/gm)];
          const recordId = [...text.matchAll(/^Record ID: `([^`\n]+)`$/gm)];
          if (upstream.length !== 1 || recordId.length !== 1 || upstream[0]![1] !== url) continue;
          // The bytes read here must be the bytes the act bound, not a later edit.
          const bound = live.filter(r => r.recordId === recordId[0]![1] && r.digest === sha256(text));
          for (const r of bound) found.add(r.repositoryId!);
        }
        return [...found].sort();
      } catch { return []; }
    },
    inForceEgress: async requirement => {
      try {
        const hits = inForceRecords(await reader.read(), options.now())
          .filter(r => r.class === 'egress' && r.project === CONSENTING_PROJECT && r.providerId === 'anthropic' && r.admittedRepositories.includes(requirement.repositoryId));
        return hits.length === 1 ? { record: `${hits[0]!.recordId}@${hits[0]!.version}`, digest: hits[0]!.digest } : null;
      } catch { return null; }
    },
  };
}
