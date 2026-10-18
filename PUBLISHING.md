# Publishing v0.1.0

These are maintainer instructions, not authorization to execute remote writes. Obtain explicit approval before creating a GitHub repository, pushing code, changing settings or visibility, publishing a release, or posting an announcement. Before each GitHub write, show the destination, affected files/settings, and intended action. Stop if the destination or local state differs from what was reviewed.

## 1. Freeze and check the candidate locally

Run from this repository with Python 3.10+, Git, Gitleaks 8.30.1, and an authenticated GitHub CLI available for later steps. Do not paste tokens into commands or commits.

```bash
python3 scripts/check_skill.py
python3 scripts/package.py
python3 scripts/package.py --check
gitleaks dir . --redact=100 --no-banner --ignore-gitleaks-allow
gitleaks git . --log-opts="--all" --redact=100 --no-banner --ignore-gitleaks-allow
git diff --check
git status --short
git log -1 --format='%H%n%an <%ae>%n%cn <%ce>%n%s'
```

The prepared candidate has a local commit, with `itstinatao` and a GitHub noreply address as author/committer. Review attribution before uploading. `git status --short` must be empty; `dist/` is intentionally ignored. Record the reviewed commit ID and the ZIP hash in your release audit. Any source change requires a new commit, rebuilt package, and renewed scans. Do not create an empty or synthetic history just to bypass a missing-history check.

Review [RELEASE_NOTES.md](RELEASE_NOTES.md), the [fictional sample](examples/sample-research-report.md), [LICENSE](LICENSE), and [LAUNCH.md](LAUNCH.md). Confirm ownership/permission to license the supplied material under MIT.

## 2. Create the private repository — approval required

Destination: `itstinatao/market-opportunity-research`. Action: create an empty **private** repository and add its remote locally. No code is uploaded by this command.

First inspect the destination and local remotes. A 404 may mean absent or inaccessible; resolve access errors before proceeding.

```bash
gh repo view itstinatao/market-opportunity-research --json nameWithOwner,visibility
git remote -v
```

If the repository does not exist and creation is approved:

```bash
gh repo create itstinatao/market-opportunity-research --private --source=. --remote=origin \
  --description 'A portable Agent Skill for evidence-backed market research, competitor mapping, business-model tradeoffs, and first-customer validation.'
```

If the repository already exists, verify its owner, visibility, contents, and history first. Do not overwrite it or force-push; reconcile differences and re-audit any additional history. Add `origin` only after verifying its URL and only if it does not already exist.

## 3. Upload the reviewed commit privately — approval required

Destination: the same private repository, branch `main`. Affected files: exactly those listed by `git ls-tree -r --name-only HEAD`; generated ZIPs and private audit reports are excluded.

```bash
git ls-tree -r --name-only HEAD
git remote get-url origin
git status --short
git push -u origin main
```

Check that the remote URL is exactly the approved destination and the working tree is clean before pushing. Do not push tags yet.

Read-only verification:

```bash
gh repo view itstinatao/market-opportunity-research --json nameWithOwner,visibility
release_commit=$(git rev-parse HEAD)
gh run list --repo itstinatao/market-opportunity-research --commit "$release_commit"
```

Wait for both `Validate skill` and `Gitleaks` on that exact commit. Use `gh run watch RUN_ID --repo itstinatao/market-opportunity-research --exit-status` for each observed run ID. Inspect the Files tab and history, including author email. A local pass does not prove GitHub Actions has run.

## 4. Prepare public settings — approval required

Destination: repository settings; no source file changes. Proposed topics are in [LAUNCH.md](LAUNCH.md).

```bash
gh repo edit itstinatao/market-opportunity-research \
  --add-topic agent-skills --add-topic market-research --add-topic business-research \
  --add-topic product-strategy --add-topic indie-hacking --add-topic ai-agents --add-topic codex
```

Confirm available security features for the repository. Enable private vulnerability reporting before launch if available; if GitHub only exposes it after visibility changes, enable and verify it immediately afterwards, before announcing. Do not claim the reporting channel is enabled until verified.

## 5. Make the repository public — separate approval required

Destination: repository visibility. Impact: **every uploaded commit and file becomes public**, not just the release ZIP. Forks, clones, and caches cannot reliably be recalled. Reconfirm the exact commit, both passing workflow runs, ownership/licensing, public attribution, and asset checksum first.

```bash
gh repo edit itstinatao/market-opportunity-research --visibility public --accept-visibility-change-consequences
```

Enable and verify the private reporting form if it was unavailable privately:

```bash
gh api --method PUT repos/itstinatao/market-opportunity-research/private-vulnerability-reporting
gh api repos/itstinatao/market-opportunity-research/private-vulnerability-reporting
```

The PUT is a separate GitHub write requiring approval. Review the public repository logged out before releasing or announcing.

## 6. Tag and publish — approval required

Destination: Git tag `v0.1.0` and a GitHub Release containing the reviewed ZIP, `SHA256SUMS`, and the text in `RELEASE_NOTES.md`. Stop if the tag already exists or points elsewhere. Never silently move a published version tag.

```bash
python3 scripts/package.py --check
git status --short
git tag --list v0.1.0
git ls-remote --tags origin refs/tags/v0.1.0
release_commit=$(git rev-parse HEAD)
git tag -a v0.1.0 "$release_commit" -m 'Market Opportunity Research v0.1.0'
git push origin refs/tags/v0.1.0
gh release create v0.1.0 --repo itstinatao/market-opportunity-research \
  --verify-tag --draft --title 'v0.1.0 — Market Opportunity Research' \
  --notes-file RELEASE_NOTES.md \
  dist/market-opportunity-research-v0.1.0.zip dist/SHA256SUMS
```

Review the draft assets and notes before the final publication write:

```bash
gh release edit v0.1.0 --repo itstinatao/market-opportunity-research --draft=false
```

Do not add `--clobber` to replace reviewed assets. If content changes, rebuild, re-scan, and obtain approval for the new artifact.

## 7. Verify the published installation, then approve the announcement

Download the published ZIP and checksum into a fresh directory. Verify the checksum, inspect the archive contents, extract it, and follow the README in an isolated skill directory. Confirm discovery and try a broad idea plus a narrow competitor question. Disclose unavailable browsing instead of inventing market facts.

Only then post the [launch announcement](LAUNCH.md), with separate approval for the destination and exact text. None of the commands above posts it.

## Rollback and withdrawal

**Before uploading:** keep the original source folder and ZIP. Discard or revise the isolated local candidate; no remote rollback is needed. Do not delete unrelated work.

**After a private upload:** stop publication. Correct the files in a normal commit, rebuild, and rerun scans/CI. Avoid force-pushes. Delete a mistaken draft release only after approval and verifying its destination.

**After a public release:** first stop announcements and explain the issue to users. For an ordinary defect, prepare `v0.1.1` with a normal corrective commit and new artifacts; keep released tags immutable. Users can remove the installed skill or restore a trusted previous copy. This first release has no earlier supported release to downgrade to.

If withdrawal is necessary, after explicit approval remove the release and assets while retaining the version tag as historical evidence:

```bash
gh release delete v0.1.0 --repo itstinatao/market-opportunity-research --yes
```

Do not use `--cleanup-tag`, move the old tag, or reuse `v0.1.0` for different bytes. Follow with an approved README notice and a new version when ready. Removing a release or making a repository private cannot recall downloaded copies, forks, or cached history.

**For a credential or private-data exposure:** revoke/rotate credentials immediately, restrict further distribution, and follow [SECURITY.md](SECURITY.md). History rewriting and coordinated cache removal require a separate reviewed plan; reverting one commit or deleting the release alone is insufficient.
