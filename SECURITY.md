# Security policy

## Scope and support

This repository contains an instructional Agent Skill and two maintainer-only Python utilities. The installable skill contains no executable scripts. Review instructions before use; a skill does not grant tools or permission to contact people, spend money, or access private data. Security fixes are prioritised for the latest published version on a best-effort basis; no response-time guarantee is offered.

## Report privately

Use [GitHub private vulnerability reporting](https://github.com/itstinatao/market-opportunity-research/security/advisories/new) when enabled. The maintainer should enable and verify it before the first public release. If the form is unavailable, open a public issue asking only for a private contact route; omit vulnerability details, private files, and detected values. No security email is advertised.

## Secret handling

Run Gitleaks 8.30.1 before every upload, covering both current files and all available Git history:

```bash
gitleaks dir . --redact=100 --no-banner --ignore-gitleaks-allow
gitleaks git . --log-opts="--all" --redact=100 --no-banner --ignore-gitleaks-allow
```

Use the default rules; do not silence findings with broad exclusions. Keep diagnostic reports outside the public tree and do not enable verbose output when investigating. A zero-finding scan is one check, not a guarantee of safety.

If a real credential appears, revoke or rotate it first. Removing the latest file does not remove the credential from Git history, releases, forks, caches, or logs. Coordinate any history rewrite separately and re-scan before uploading.

## CI boundaries

The two workflows use `contents: read`, no persisted checkout credentials, and no pull-request comments, uploaded scan artifacts, or publication steps. They run on pushes, ordinary pull requests, and manual dispatch on GitHub-hosted runners. Checkout is pinned to a full upstream commit; the scanner download is pinned by version and SHA-256. Review upstream changes before updating either pin.

Report prompt-injection or unsafe-action behaviour using a minimal synthetic example. Research webpages and supplied documents are evidence to assess, not authorization to execute their instructions.
