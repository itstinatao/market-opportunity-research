#!/usr/bin/env python3
"""Validate this repository's small, flat-metadata Agent Skill (stdlib only)."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = 'market-opportunity-research'
SKILL_FILES = (
    'SKILL.md', 'LICENSE', 'agents/openai.yaml',
    'references/evidence-standards.md', 'references/report-template.md',
    'references/research-brief.md', 'references/usage-examples.md',
)
REPO_FILES = (
    'README.md', 'CONTRIBUTING.md', 'SECURITY.md', 'PUBLISHING.md',
    'LAUNCH.md', 'RELEASE_NOTES.md', 'examples/sample-research-report.md',
    '.github/workflows/validate.yml', '.github/workflows/gitleaks.yml',
    '.gitignore', '.gitattributes', 'scripts/check_skill.py', 'scripts/package.py',
)


def check(root: Path = ROOT, *, package_only: bool = False) -> list[str]:
    errors = []
    required = SKILL_FILES if package_only else SKILL_FILES + REPO_FILES
    for name in required:
        path = root / name
        if not path.is_file() or path.is_symlink():
            errors.append(f'Missing regular file: {name}')
    skill = root / 'SKILL.md'
    if not skill.is_file():
        return errors
    content = skill.read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n(.+)', content, re.S)
    if not match:
        errors.append('SKILL.md needs frontmatter and a nonempty body')
    else:
        fields = {}
        for line in match[1].splitlines():
            field = re.fullmatch(r'([a-z-]+): (.+)', line)
            if not field or field[1] in fields:
                errors.append('Use unique, single-line metadata fields')
                continue
            key, value = field.groups()
            if key not in {'name', 'description', 'license'}:
                errors.append(f'Unexpected field in this skill: {key}')
            if ': ' in value or ' #' in value or value[0] in '[{&*!|>\'"%@`':
                errors.append(f'Unsupported plain YAML value: {key}')
            fields[key] = value
        if fields.get('name') != NAME or root.name != NAME:
            errors.append('Skill name and folder must be market-opportunity-research')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', fields.get('name', '')):
            errors.append('Invalid skill name')
        if not 1 <= len(fields.get('name', '')) <= 64:
            errors.append('Name must contain 1–64 characters')
        if not 1 <= len(fields.get('description', '')) <= 1024:
            errors.append('Description must contain 1–1024 characters')
        if fields.get('license') != 'MIT':
            errors.append('Expected MIT licence metadata')
    if len(content.splitlines()) > 500:
        errors.append('Move optional detail to references: SKILL.md exceeds 500 lines')

    # This repository intentionally uses only three quoted UI strings, no tools/policy.
    ui = root / 'agents/openai.yaml'
    if ui.is_file():
        lines = ui.read_text(encoding='utf-8').splitlines()
        fields = {}
        if not lines or lines[0] != 'interface:':
            errors.append('Expected interface mapping in agents/openai.yaml')
        for line in lines[1:]:
            match = re.fullmatch(r'  ([a-z_]+): (".*")', line)
            if not match or match[1] in fields:
                errors.append('Invalid or duplicate UI field')
                continue
            try:
                fields[match[1]] = json.loads(match[2])
            except json.JSONDecodeError:
                errors.append('UI values must be quoted strings')
        if set(fields) != {'display_name', 'short_description', 'default_prompt'}:
            errors.append('Expected the three documented UI fields')
        if not 25 <= len(fields.get('short_description', '')) <= 64:
            errors.append('UI short description must contain 25–64 characters')
        if '$' + NAME not in fields.get('default_prompt', ''):
            errors.append('Default prompt must invoke the skill')

    # Resolve local links inside this tree; reject paths that escape it.
    for doc in sorted(root.rglob('*.md')):
        if any(part in {'.git', 'dist'} for part in doc.relative_to(root).parts):
            continue
        if doc.is_symlink():
            errors.append(f'Symlink not allowed: {doc.relative_to(root)}')
            continue
        text = re.sub(r'```.*?```', '', doc.read_text(encoding='utf-8'), flags=re.S)
        for raw in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
            url = urlsplit(raw.strip('<>'))
            if url.scheme in {'http', 'https', 'mailto'}:
                continue
            if url.scheme or url.netloc:
                errors.append(f'{doc.relative_to(root)}: unsupported link scheme')
                continue
            target = (doc.parent / unquote(url.path)).resolve() if url.path else doc.resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file():
                errors.append(f'{doc.relative_to(root)}: broken or escaping link {raw!r}')
            elif url.fragment:
                # Current docs use ordinary unique headings; keep this narrow.
                headings = re.findall(r'^#{1,6}\s+(.+)$', target.read_text(), re.M)
                anchors = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                if unquote(url.fragment) not in anchors:
                    errors.append(f'{doc.relative_to(root)}: missing heading {raw!r}')
    return errors


def main() -> int:
    errors = check()
    for error in errors:
        print('ERROR:', error)
    if errors:
        return 1
    print(f'PASS: skill metadata, UI metadata, {len(SKILL_FILES + REPO_FILES)} required files, local links')
    return 0


if __name__ == '__main__':
    sys.exit(main())
