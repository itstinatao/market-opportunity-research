# Contributing

Useful contributions improve buyer framing, source evaluation, commercial tradeoffs, or actionable validation. Explain the observable failure and give a small public or fictional example. Keep the skill portable and the repository dependency-light.

## Before submitting

- Preserve narrow-question support; do not turn one example into a universal requirement.
- Put optional detail in references and link it from `SKILL.md`.
- Use only material you may redistribute under MIT. Do not paste private research, customer data, credentials, or unlicensed reports.
- Run the commands below with Python 3.10+ and Gitleaks 8.30.1. Inspect findings privately; never paste detected values into an issue.

```bash
python3 scripts/check_skill.py
python3 scripts/package.py
python3 scripts/package.py --check
gitleaks dir . --redact=100 --no-banner --ignore-gitleaks-allow
gitleaks git . --log-opts="--all" --redact=100 --no-banner --ignore-gitleaks-allow
```

Directory scanning covers current changes; history scanning covers commits. Re-run history scanning after committing. For instruction changes, also try a relevant prompt and a narrow question; describe the result and its limits. Passing structural checks alone does not prove research quality.

## Pull request contents

State the problem, proposed behaviour, a before/after example, checks actually run, and remaining limitations. Small focused changes are easier to review. Do not add build tooling or scheduled workflows without a concrete need.

Submitting a contribution confirms that you have the right to contribute it under the repository's MIT licence. Review is on a best-effort basis. Report security issues using [SECURITY.md](SECURITY.md), not public issue details.
