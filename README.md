# Market Opportunity Research

**Turn a business idea into an evidence-backed decision and a practical first-customer experiment.**

A portable Agent Skill that guides an AI agent through buyer problems, demand evidence, real competitors, commercial tradeoffs, and what to test next. Bring an idea and an agent with research access. The skill supplies the process; your agent supplies the research tools.

## See the output

Ask:

> Use $market-opportunity-research to evaluate a quote-follow-up service for small repair businesses. Compare service-first and software-first options, show the evidence gaps, and propose a small paid pilot.

A report connects **buyer → evidence → alternatives → commercial options → experiment**. It labels facts, vendor claims, inferences, and hypotheses, and explains what would change the recommendation.

From the [fictional sample report](examples/sample-research-report.md):

> Start with a manually delivered follow-up pilot before building software. In this fictional scenario, the decisive uncertainty is whether owners will pay for the service, not whether reminders can be automated. A proposed $150 pilot is a pricing hypothesis; no customer has paid it.

The sample demonstrates the format and reasoning. All its organisations, numbers, and events are invented; it is not market evidence. For real research, the skill calls for dated sources, named competitors, documented customer examples, and counter-evidence.

## Install

The release contains a single `market-opportunity-research/` folder following the [Agent Skills specification](https://agentskills.io/specification). It has Markdown instructions, references, optional Codex UI metadata, and an MIT licence. **No executable scripts, credentials, or bundled services are in the skill ZIP.**

### Codex: release ZIP (recommended)

1. Download `market-opportunity-research-v0.1.0.zip` and `SHA256SUMS` from the [v0.1.0 release](https://github.com/itstinatao/market-opportunity-research/releases/tag/v0.1.0). These links become available when the release is published.
2. In the download directory, check the archive: `shasum -a 256 -c SHA256SUMS` on macOS, or `sha256sum -c SHA256SUMS` on Linux.
3. Extract and read `SKILL.md`. Copy the extracted folder into `~/.agents/skills/` for personal use, or `.agents/skills/` inside a project for project use. Do not overwrite an existing installation without comparing or backing it up.
4. Invoke the skill by name as shown below. If it does not appear, restart Codex.

These locations follow the [official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills). Use your client's documented skill directory if it differs. Avoid installing the same skill in multiple discovery locations.

### Codex: clone a tagged version

After `v0.1.0` is published, an alternative is:

```bash
mkdir -p ~/.agents/skills
git clone --branch v0.1.0 --depth 1 \
  https://github.com/itstinatao/market-opportunity-research.git \
  ~/.agents/skills/market-opportunity-research
```

Cloning also includes maintainer scripts and repository documentation. The skill does not instruct agents to execute those scripts. Git refuses to clone into an existing nonempty directory.

### Other compatible agents

Use the release ZIP or copy its extracted folder to the skill directory documented by your client. Import interfaces vary; this project does not claim universal one-click installation or ship a ChatGPT plugin bundle. Without skill support, provide `SKILL.md` and its referenced files as context and explicitly ask the agent to follow the workflow.

## Use

```text
Use $market-opportunity-research to evaluate [idea].
My target buyer is [buyer], in [region].
I have [time, budget, expertise or prototype].
Help me decide [decision], using current sources and a small paid validation plan.
```

One sentence is enough to start. The [optional research brief](references/research-brief.md) helps scope a deeper investigation. Narrow questions receive focused answers rather than a full report.

- **Market map:** “Who already solves this buyer problem, including services and manual alternatives?”
- **Business model:** “Compare a service, a niche product, and a partnership for this idea.”
- **Founder journey:** “What public evidence explains how this company acquired its first paying customers?”

See [usage examples](references/usage-examples.md), [evidence standards](references/evidence-standards.md), and the [flexible report outline](references/report-template.md).

## Limitations

Current research requires browsing or equivalent research tools; without them, output should be a hypothesis map. Public prices do not establish realised deal sizes, vendor case studies are not independent proof, and plausible gaps are not validated demand. The skill cannot guarantee profitable ideas or replace customer interviews. Any outreach or paid experiment needs your authorization. Agent behaviour and source quality still require review.

## For contributors

Python 3.10+ is enough for the two standard-library-only maintainer scripts. Install [Gitleaks](https://github.com/gitleaks/gitleaks/releases/tag/v8.30.1) separately for secret scans; CI pins version 8.30.1.

```bash
python3 scripts/check_skill.py
python3 scripts/package.py
python3 scripts/package.py --check
gitleaks dir . --redact=100 --no-banner --ignore-gitleaks-allow
gitleaks git . --log-opts="--all" --redact=100 --no-banner --ignore-gitleaks-allow
```

The last check requires Git history. The package and checksum are written to ignored `dist/`. GitHub Actions validates the package and scans files/history with read-only repository access. A clean scan is not proof that every sensitive item is absent.

Read [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and the maintainer [publishing checklist](PUBLISHING.md).

## Licence

[MIT](LICENSE), copyright 2026 itstinatao. Independent project; not affiliated with or endorsed by an AI platform vendor.
