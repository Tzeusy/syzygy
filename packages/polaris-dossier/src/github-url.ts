/** The repository URL the operator names, parsed and never fetched (design "Command surface": "the URL is parsed, not fetched").
 *
 * Copied from `parseGithubUrl` in apps/three-surface-poc/src/polaris-generation/dossier-trigger.ts, which a package cannot import;
 * the two copies are one rule and change together. The URL is configuration that finds the observation consent whose `Upstream:`
 * names it; it is never the repository's identity, which only that consent's subject gives. */

export interface GithubTarget { readonly owner: string; readonly repo: string; readonly ref?: string; readonly url: string; readonly repositoryId: string }

/** Public https://github.com/<owner>/<repo> only, optionally `/tree/<ref>`. No credentials, no other host. */
export function parseGithubUrl(input: string): GithubTarget {
  const match = /^https:\/\/github\.com\/([A-Za-z0-9][A-Za-z0-9-]{0,38})\/([A-Za-z0-9._-]{1,100}?)(?:\.git)?(?:\/tree\/([A-Za-z0-9._\/-]{1,200}))?\/?$/u.exec(input);
  if (match === null || match[2] === '.' || match[2] === '..' || (match[3] ?? '').split('/').some(part => part === '..')) throw new Error('invalid-github-url');
  const [, owner, repo, ref] = match as unknown as [string, string, string, string | undefined];
  return { owner, repo, ...(ref === undefined ? {} : { ref }), url: `https://github.com/${owner}/${repo}`, repositoryId: `github:${owner}:${repo.replace(/[_.]/gu, ch => (ch === '_' ? '__' : '_d'))}` };
}

/** The canonical URL for a dossier command, or why the input is not one. A `/tree/<ref>` form is refused: the run's revision is the
 * clone's HEAD, checked against the revisions the consent names, so a ref in the URL would be a second, unchecked choice. */
export function dossierRepositoryUrl(input: string): { readonly ok: true; readonly url: string } | { readonly ok: false; readonly reason: string } {
  let target: GithubTarget;
  try {
    target = parseGithubUrl(input);
  } catch {
    return { ok: false, reason: `${JSON.stringify(input.slice(0, 200))} is not a public https://github.com/<owner>/<repo> URL` };
  }
  if (target.ref !== undefined) {
    return { ok: false, reason: `the URL names the ref ${target.ref}; name the repository only — the run's revision is the clone's HEAD, which must be a revision the observation consent names` };
  }
  return { ok: true, url: target.url };
}
